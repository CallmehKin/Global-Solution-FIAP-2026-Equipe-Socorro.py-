# Roteiro do vídeo — Citizen Assist AI | Grupo 9 (≈ 6 min)

## Preparação
- VS Code com tema escuro, fonte ampliada (Ctrl + `=` duas vezes) e terminal integrado aberto (Ctrl + `) na pasta raiz do projeto.
- Fechar e-mail, WhatsApp e abas com dados pessoais.
- Deixar abertos em abas: `README.md`, `data/base.json`, `src/sistema.py`, `docs/comparacao_modelos.md`, `docs/teste_usabilidade.md`.
- Publicar no YouTube como **Não listado**.

---

## 1. Abertura (0:00–0:40) — Isaac
**Tela:** `README.md` em Preview (Ctrl+Shift+V), mostrando título e equipe.

> "Oi, somos o Grupo 9, equipe Socorro.py: Isaac, Julia e Samirah. Este é o Citizen Assist AI, um protótipo que ajuda a encontrar orientações sobre CIN, CPF e conta GOV.BR, sempre com a fonte oficial. Ele não é um canal do governo."

## 2. Problema e escopo (0:40–1:20) — Julia
**Tela:** README, seções "Problema, público e escopo" e "Fontes, acessibilidade e privacidade".

> "As informações sobre documentos e serviços digitais ficam espalhadas. Nossa base tem 20 orientações em 3 temas: Documentos, Serviços digitais e Direitos e acesso. O sistema funciona offline e não pede CPF, senha nem nenhum dado pessoal."

## 3. Como funciona (1:20–2:20) — Samirah
**Tela:**
- `data/base.json` → primeiro registro; destacar `referencia` e `verificado_em`.
- `src/sistema.py` → função `carregar` (validação), `buscar` (limiar 0,49) e `RELACOES`.

> "Cada orientação tem tema, palavras-chave, link oficial e data de verificação. Ao iniciar, o sistema valida a base. Depois compara a pergunta com a base por similaridade de texto e só responde quando a nota passa de 0,49. Se não encontra, diz isso; se a pergunta fica entre dois assuntos, pede para especificar."

## 4. Demonstração (2:20–3:50) — Julia
**Tela:** terminal → `python src/sistema.py`

| Digitar | Fala |
|---|---|
| `P` → `A conta GOV.BR é gratuita?` | "A resposta traz orientação, fonte, data e aviso." |
| `P` → `identidade cpf` | "Pergunta ambígua: ele pede esclarecimento e sugere opções." |
| `P` → `Como solicitar licença para construir em Marte?` | "Fora da base, ele não inventa resposta." |
| `9` | "Opção inválida no menu também é tratada." |
| `2` (Documentos) → `Como consultar a situação do CPF?` | "Escolhendo um tema, aparecem subtemas e temas relacionados." |
| `S` | — |

## 5. Testes e avaliação (3:50–4:50) — Isaac
**Tela:**
- `python -m unittest discover -s tests -v` → 11 testes OK.
- `python tests/avaliar.py` → abrir `docs/resultados_testes.csv`.
- `docs/comparacao_modelos.md` → tabela A × B.

> "Temos 11 testes automáticos e 18 perguntas de avaliação: diretas, fora da base, inválida e ambígua. Acertamos 18 de 18, mas isso vale para perguntas conhecidas, não para perguntas novas. Comparamos dois formatos de resposta e escolhemos o B, porque mostra fonte, data e aviso."

## 6. Avaliação de usabilidade (4:50–5:40) — Samirah
**Tela:** `docs/teste_usabilidade.md` em Preview → tabela "Resultado por heurística".

> "Fizemos uma avaliação heurística com as 10 heurísticas de Nielsen, executando 8 cenários no sistema. Os pontos fortes são a transparência, já que toda resposta tem fonte, data e aviso, e o fato de o sistema não inventar resposta. Os problemas mais graves: ao escolher um tema, as perguntas disponíveis não aparecem, e termos populares como 'RG' não são reconhecidos. Como melhoria, propomos listar as perguntas numeradas por tema e ampliar os sinônimos."

## 7. Limitações e encerramento (5:40–6:20) — Isaac
**Tela:** README → "Limitações e melhorias" → repositório no GitHub.

> "A busca é heurística, então pode errar, e as informações oficiais mudam; por isso cada resposta mostra fonte e data. A avaliação heurística não substitui um teste com usuários reais, que é nosso próximo passo, junto com uma interface web acessível. Obrigado!"

---

## Depois de publicar
1. Colar o link em `docs/link_video.txt`, no README (seção "Vídeo"), no relatório PDF e no TXT de entrega.
2. Fazer commit e push e conferir o GitHub público.
