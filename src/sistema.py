"""Citizen Assist AI - protótipo educacional offline, Python 3.10+."""
import json, re, unicodedata, sys, time
from pathlib import Path
from difflib import SequenceMatcher
BASE_PADRAO = Path(__file__).resolve().parents[1] / 'data' / 'base.json'
OBRIGATORIOS = {'id','tema','subtema','pergunta','palavras_chave','orientacao','referencia','verificado_em'}
RELACOES = {'Documentos':['Serviços digitais','Direitos e acesso'],'Serviços digitais':['Documentos','Direitos e acesso'],'Direitos e acesso':['Documentos','Serviços digitais']}
def normalizar(s):
    s=unicodedata.normalize('NFKD',str(s).lower())
    return re.sub(r'[^a-z0-9 ]',' ',''.join(c for c in s if not unicodedata.combining(c))).strip()
def carregar(caminho=BASE_PADRAO):
    try:
        with open(caminho,encoding='utf-8') as f: dados=json.load(f)
    except (OSError,UnicodeError,json.JSONDecodeError) as e: raise ValueError(f'Não foi possível carregar a base: {e}') from e
    if not isinstance(dados,list) or not dados:raise ValueError('Base ausente ou vazia: é necessária uma lista de registros.')
    ids=set()
    for i,r in enumerate(dados,1):
        if not isinstance(r,dict) or not OBRIGATORIOS.issubset(r):raise ValueError(f'Registro {i}: campos obrigatórios ausentes.')
        if any(not isinstance(r[k],str) or not r[k].strip() for k in OBRIGATORIOS-{'palavras_chave'}):raise ValueError(f'Registro {i}: campo de texto vazio/inválido.')
        if not isinstance(r['palavras_chave'],list) or not r['palavras_chave'] or any(not isinstance(x,str) or not x.strip() for x in r['palavras_chave']):raise ValueError(f'Registro {i}: palavras-chave inválidas.')
        if not r['referencia'].startswith('https://'):raise ValueError(f'Registro {i}: referência inválida.')
        if r['id'] in ids:raise ValueError(f'Registro {i}: identificador duplicado.')
        ids.add(r['id'])
    return dados
def conceitos(pergunta):
    """Normaliza variações frequentes sem depender de APIs externas."""
    tokens = normalizar(pergunta).split()
    sinonimos = {'gratuita':'gratuito', 'gratis':'gratuito', 'paga':'pagamento',
                 'pagar':'pagamento', 'cobrada':'pagamento', 'govbr':'gov',
                 'identidades':'identidade'}
    return {sinonimos.get(t, t) for t in tokens}

def consulta_ambigua(pergunta):
    """Consulta telegráfica com dois documentos e sem intenção identificável."""
    tokens = conceitos(pergunta)
    return len(tokens) <= 3 and {'identidade', 'cpf'} <= tokens

def pontuar(pergunta,registro):
    q=normalizar(pergunta); tokens=conceitos(pergunta); campos=[registro['pergunta']]+registro['palavras_chave']; melhor=0.0
    for campo in campos:
        c=normalizar(campo); ct=conceitos(campo); sobreposicao=len(tokens & ct)/max(1,len(ct)); semelhanca=SequenceMatcher(None,q,c).ratio()
        score=max(semelhanca*0.72, sobreposicao*0.88)
        if q==c:score=1.0
        if c in q and len(c)>=8:score=max(score,0.91)
        melhor=max(melhor,score)
    return melhor
def buscar(pergunta,base,tema=None):
    if not isinstance(pergunta,str) or not pergunta.strip():return {'status':'invalida','mensagem':'Digite uma pergunta ou escolha um tema.'}
    if len(pergunta)>500:return {'status':'invalida','mensagem':'Pergunta muito longa (máximo 500 caracteres).'}
    if consulta_ambigua(pergunta):return {'status':'ambigua','mensagem':'Você quer saber sobre identidade ou CPF? Especifique o serviço ou a dúvida.','opcoes':['Como emitir a CIN?','Como consultar o CPF?']}
    candidatos=[r for r in base if tema is None or r['tema']==tema]
    if not candidatos:return {'status':'invalida','mensagem':'Tema inexistente. Escolha um tema do menu.'}
    ordenados=sorted(((pontuar(pergunta,r),r) for r in candidatos),key=lambda x:(-x[0],x[1]['id']))
    score,registro=ordenados[0]
    # Intenção explícita de gratuidade tem precedência sobre perguntas genéricas
    # sobre a conta GOV.BR, desde que exista registro específico na base.
    tokens=conceitos(pergunta)
    if 'conta' in tokens and 'gov' in tokens and ('gratuito' in tokens or 'pagamento' in tokens):
        especificos=[r for r in candidatos if r['id']=='ORI-015']
        if especificos:
            registro=especificos[0]
            score=max(score,0.92)
            ordenados=[(score,registro)]+[(s,r) for s,r in ordenados if r['id']!='ORI-015']

    if score<0.49:return {'status':'sem_resposta','mensagem':'Não encontrei orientação confiável na base para essa pergunta. Consulte os canais oficiais ou escolha outro assunto.','alternativas':sorted(set(r['tema'] for r in base))}
    if not (registro['id']=='ORI-015' and 'conta' in tokens and 'gov' in tokens and ('gratuito' in tokens or 'pagamento' in tokens)) and len(ordenados)>1 and ordenados[1][0]>=0.49 and score-ordenados[1][0]<0.075 and ordenados[1][1]['subtema']!=registro['subtema']:
        return {'status':'ambigua','mensagem':'Sua pergunta pode se referir a mais de um assunto. Especifique o documento ou serviço.','opcoes':[x[1]['pergunta'] for x in ordenados[:3]]}
    return {'status':'ok','registro':registro,'pontuacao':round(score,3),'relacionados':RELACOES.get(registro['tema'],[])}
def formatar(resultado,modelo='B'):
    if resultado['status']!='ok':return resultado['mensagem']+'\n'+'\n'.join(resultado.get('opcoes',resultado.get('alternativas',[])))
    r=resultado['registro']
    if modelo=='A':return r['orientacao']+'\nFonte: '+r['referencia']
    return ('ORIENTAÇÃO: '+r['orientacao']+'\nFONTE: '+r['referencia']+'\nVERIFICAÇÃO: '+r['verificado_em']+'\nATENÇÃO: '+r.get('aviso','Confirme a informação na fonte oficial.')+'\nOUTROS TEMAS: '+', '.join(resultado['relacionados']))
def consultar(pergunta,base,tema=None,modelo='B'):
    inicio=time.perf_counter(); resultado=buscar(pergunta,base,tema); resultado['tempo_ms']=round((time.perf_counter()-inicio)*1000,4)
    resultado['texto']=formatar(resultado,modelo);return resultado
def menu(base):
    temas=sorted(set(r['tema'] for r in base))
    while True:
        print('\n=== CITIZEN ASSIST AI | PROTÓTIPO EDUCACIONAL ===')
        print('Não é canal oficial. Não informe dados pessoais.')
        for i,t in enumerate(temas,1):print(f'{i}. {t}')
        print('P. Pergunta livre | S. Sair')
        escolha=input('Opção: ').strip().lower()
        if escolha=='s':break
        if escolha=='p':tema=None
        elif escolha.isdigit() and 1<=int(escolha)<=len(temas):tema=temas[int(escolha)-1]
        else:print('Opção inválida.');continue
        if tema:
            print('Subtemas:',', '.join(sorted(set(r['subtema'] for r in base if r['tema']==tema))))
            print('Relacionados:',', '.join(RELACOES.get(tema,[])))
        pergunta=input('Pergunta: ')
        resposta=consultar(pergunta,base,tema)
        print('\n'+resposta['texto'])
        print(f"Tempo de busca: {resposta['tempo_ms']:.4f} ms")
def main():
    try:base=carregar(Path(sys.argv[1]) if len(sys.argv)>1 else BASE_PADRAO)
    except ValueError as e:print('ERRO:',e);return 1
    menu(base);return 0
if __name__=='__main__':sys.exit(main())
