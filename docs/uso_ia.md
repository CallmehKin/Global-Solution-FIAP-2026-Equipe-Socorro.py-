# Uso de IA e validação crítica

Ferramenta utilizada no desenvolvimento: ChatGPT (OpenAI), para planejamento, redação inicial, estrutura de código e proposta de testes. Nenhuma API externa de IA é chamada pelo protótipo em execução.

## Modelos de instrução de resposta

**Modelo A — resposta curta:** "Responda exclusivamente com a orientação recuperada da base e a URL da fonte. Não acrescente informação não presente no registro."

**Modelo B — resposta estruturada:** "Apresente ORIENTAÇÃO, FONTE, DATA DE VERIFICAÇÃO, AVISO DE LIMITAÇÃO e TEMAS RELACIONADOS. Não invente conteúdo; se não houver correspondência suficiente, informe a limitação."

Os modelos são **templates determinísticos** implementados em `formatar` e não prompts enviados a um modelo generativo. A comparação pode ser reproduzida com `formatar(resultado, 'A')` e `formatar(resultado, 'B')`. O modelo B foi escolhido pelo critério de rastreabilidade: exibe data, fonte e aviso; a clareza deve ser validada no teste humano de usabilidade.

## Validação

Fontes institucionais identificadas em `data/base.json`; conferir periodicamente URLs, atualizações e requisitos estaduais. Respostas devem ser confrontadas com os textos oficiais antes da entrega. Não foram feitas alegações de atendimento oficial ou de execução de IA generativa.

## Limitações

Busca heurística por similaridade, sem compreensão semântica robusta; informações podem mudar. É possível ocorrer falso positivo. O sistema não solicita CPF, senha ou dados pessoais.
