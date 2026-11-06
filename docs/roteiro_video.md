# Roteiro de apresentação — Citizen Assist AI (5–7 minutos sugeridos)

**0:00–0:40 — Apresentação.** "Somos o Grupo 9, equipe Socorro.py. Nosso projeto Citizen Assist AI facilita a consulta de orientações cidadãs com referências identificáveis. Não somos um canal oficial."

**0:40–1:30 — Problema e público.** Mostrar o README e explicar informações dispersas, escopo, privacidade e três temas.

**1:30–2:30 — Arquitetura.** Mostrar `data/base.json` (20 registros, fonte e data), `src/sistema.py` (busca e validação), grafo de temas e `tests/`.

**2:30–4:20 — Demonstração real.** No terminal executar `python src/sistema.py`. Perguntar "A conta GOV.BR é gratuita?" e mostrar fonte. Perguntar "identidade cpf" e mostrar pedido de esclarecimento. Perguntar sobre licença para construir em Marte e mostrar limite. Demonstrar opção inválida no menu.

**4:20–5:30 — Avaliação.** Executar `python -m unittest discover -s tests -v` e `python tests/avaliar.py`. Mostrar resultados atualizados; explicar que 18/18 é desempenho no conjunto conhecido, não em perguntas inéditas. Exibir comparação A/B em `docs/comparacao_modelos.md`.

**5:30–6:30 — Limitações e encerramento.** Explicar busca heurística, atualização das fontes e resultados do teste real de usabilidade **somente depois de realizado**. Agradecer e mostrar o repositório.

Gravar a tela com texto legível, áudio claro e evitar exibir senhas ou dados pessoais. Publicar como **Não listado** e atualizar `docs/link_video.txt`, README e arquivo de entrega da FIAP.
