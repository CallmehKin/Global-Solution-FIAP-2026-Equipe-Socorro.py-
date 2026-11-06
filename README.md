# Citizen Assist AI — Global Solution 2026.2 | Grupo 9

Continuação acadêmica do repositório `globalsolution_grupo9`. **Este protótipo é independente e não representa órgão público.**

**Equipe / RMs:** 

Isaac Aurélio de Freitas Castro | RM 571175

Julia Guimarães | RM 572241

Samirah Pinotti Deranian | RM 573375

Luiz Pedro Pereira Duarte | RM 568970

## Problema, público e escopo

Pessoas que buscam informações confiáveis sobre documentos, conta GOV.BR e acesso a serviços públicos encontram instruções dispersas. O sistema oferece consulta offline a uma base JSON de 20 orientações em 3 temas: Documentos, Serviços digitais e Direitos e acesso. Não solicita dados pessoais.

## Como executar

Python 3.10+; sem dependências externas. A partir desta pasta:

```bash
python src/sistema.py
python -m unittest discover -s tests -v
python tests/avaliar.py
```

## Organização e algoritmos

- `data/base.json`: lista de dicionários com identificador, tema, subtema, pergunta, palavras-chave, orientação, referência HTTPS e data de verificação. Acrescente registros editando somente JSON.
- `src/sistema.py`: valida JSON, cria menu, busca por similaridade de texto (`SequenceMatcher`) e sobreposição de palavras; retorna uma resposta apenas acima do limiar 0,49; sinaliza ambiguidade entre subtemas.
- `RELACOES`: grafo simples de 3 temas com vizinhos para continuidade de consulta.
- Complexidade: para N registros e K termos por registro, consulta percorre N registros e calcula similaridades de strings; ordenação O(N log N). Não é busca semântica e pode errar.
- `tests/avaliar.py`: 18 casos e métricas reproduzíveis de acerto e tempo de busca local.

## Modelos de resposta

A: orientação + fonte. B (padrão): orientação, fonte, data, aviso e temas relacionados. Os dois são templates determinísticos; não há API nem modelo generativo em tempo de execução. Ver `docs/uso_ia.md`.

## Exemplos

Pergunta: `O que é uma conta GOV.BR?` → resposta da base com URL oficial. Pergunta vazia → mensagem de entrada inválida. Pergunta sobre Marte → sem orientação confiável. Ambiguidade → solicitar esclarecimento.

## Avaliação

Executar `python tests/avaliar.py` para gerar `docs/resultados_testes.csv` e `docs/indicadores.json`. Os resultados são medidos na máquina em que o comando é executado. Teste de facilidade de uso: protocolo em `docs/teste_usabilidade.md` — **pendente de participante real**. O relatório PDF identifica explicitamente essa pendência.

## Fontes, acessibilidade e privacidade

Cada registro contém URL de referência institucional e data da verificação editorial. O usuário deve confirmar informações atualizadas e regras locais no canal oficial. Interface textual com menus numerados e mensagens descritivas; melhoria futura: interface web acessível e navegação por teclado. Não armazenamos perguntas nem solicitamos CPF, senha ou endereço.

## Vídeo

**Link:** [PENDENTE — adicionar URL após publicar vídeo não listado]. Roteiro em `docs/roteiro_video.md`.

## Limitações e melhorias

A base é finita, o algoritmo é heurístico e pode apresentar falsos positivos; datas e serviços podem mudar. Melhorias: limiares calibrados, sinônimos revisados, atualização periódica das fontes e teste de usabilidade ampliado.
