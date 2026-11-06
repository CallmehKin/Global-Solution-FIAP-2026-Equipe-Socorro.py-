import csv,json,sys,time
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from sistema import carregar,consultar
raiz=Path(__file__).resolve().parents[1];base=carregar();casos=json.loads((raiz/'data'/'perguntas_teste.json').read_text(encoding='utf-8'))
linhas=[]
for caso in casos:
 r=consultar(caso['pergunta'],base);obtido=r.get('registro',{}).get('id');esperado=caso['esperado']
 correto=(obtido==esperado and (esperado is not None or r['status']!='ok'))
 linhas.append(dict(id=caso['id'],categoria=caso['categoria'],pergunta=caso['pergunta'],esperado=esperado or 'SEM RESPOSTA',obtido=obtido or r['status'],correto=int(correto),tempo_ms=r['tempo_ms'],status=r['status']))
saida=raiz/'docs'/'resultados_testes.csv'
with saida.open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=linhas[0].keys());w.writeheader();w.writerows(linhas)
acertos=sum(x['correto'] for x in linhas);media=sum(x['tempo_ms'] for x in linhas)/len(linhas)
resumo={'total':len(linhas),'acertos':acertos,'taxa_acerto_percentual':round(100*acertos/len(linhas),2),'tempo_medio_ms':round(media,4),'observacao':'Mede somente a busca local; não inclui tempo humano nem rede.'}
(raiz/'docs'/'indicadores.json').write_text(json.dumps(resumo,indent=2,ensure_ascii=False),encoding='utf-8')
print(json.dumps(resumo,indent=2,ensure_ascii=False))
