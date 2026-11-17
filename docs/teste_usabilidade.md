# Avaliação de usabilidade — avaliação heurística (Nielsen)

**Método:** avaliação heurística com base nas 10 heurísticas de usabilidade de Jakob Nielsen, aplicada à interface textual de `src/sistema.py`. Não houve participante externo; os achados abaixo vêm da execução real do sistema nos cenários descritos e **não substituem um teste com usuários**.

**Data:** 16/11/2026 | **Avaliadores:** equipe do Grupo 9 (Isaac, Julia, Samirah) | **Apoio:** execução dos cenários e registro dos achados com apoio de IA (Claude), revisados pela equipe — ver `docs/uso_ia.md`.

**Escala de severidade (Nielsen):** 0 = não é problema · 1 = cosmético · 2 = pequeno · 3 = grande · 4 = catastrófico.

## Cenários executados

| # | Tarefa | Entrada | Resultado observado |
|---|---|---|---|
| 1 | Informação sobre primeira via da CIN | `P` → "Como tirar a primeira via da CIN?" | Resposta correta (ORI-002) com fonte, data e aviso |
| 2 | Níveis da conta GOV.BR | `P` → "Quais níveis existem na conta GOV.BR?" | Resposta correta (ORI-011) |
| 3 | Pergunta fora da base | `P` → "Como solicitar licença para construir em Marte?" | Informa que não há orientação confiável e lista os temas |
| 4 | Navegar por tema | `1` (Direitos e acesso) → "quem pode ter acesso?" | Mostra subtemas, mas a pergunta livre não encontrou resposta; as perguntas disponíveis do tema não são listadas |
| 5 | Termo popular | `P` → "como tirar rg" | Sem resposta: o termo "RG" não é reconhecido |
| 6 | Pergunta curta | `P` → "cpf" | Sem resposta, embora existam 4 registros sobre CPF |
| 7 | Entrada inválida / vazia | `9` e pergunta vazia | "Opção inválida." / "Digite uma pergunta ou escolha um tema." |
| 8 | Pergunta ambígua | `P` → "identidade cpf" | Pede esclarecimento e sugere 2 perguntas |

## Resultado por heurística

| Heurística | Avaliação | Severidade |
|---|---|---|
| 1. Visibilidade do status do sistema | Cada resposta mostra fonte, data de verificação e aviso; o usuário sabe de onde veio a informação. | 0 |
| 2. Correspondência com o mundo real | "RG" não é reconhecido (C5); data no formato `2026-11-05` em vez de `05/11/2026`; "Tempo de busca: x ms" é linguagem técnica. | 3 |
| 3. Controle e liberdade do usuário | Após escolher um tema, não há opção "voltar": é preciso digitar uma pergunta para retornar ao menu. | 2 |
| 4. Consistência e padrões | Menu numerado consistente; porém os temas são numerados e as sugestões (ambiguidade, sem resposta) não, e não podem ser escolhidas pelo número. | 2 |
| 5. Prevenção de erros | Aviso "Não informe dados pessoais", limite de 500 caracteres e pedido de esclarecimento em perguntas ambíguas. | 0 |
| 6. Reconhecimento em vez de memorização | Ao escolher um tema, o sistema mostra subtemas, mas não as perguntas disponíveis; o usuário precisa adivinhar como perguntar (C4, C6). | 3 |
| 7. Flexibilidade e eficiência de uso | "Outros temas" aparece só como texto, sem atalho para navegar; o menu completo é reimpresso a cada consulta. | 2 |
| 8. Estética e design minimalista | Respostas curtas e organizadas por rótulos; o tempo em ms e URLs muito longas (ORI-012) poluem a leitura. | 1 |
| 9. Reconhecer, diagnosticar e recuperar-se de erros | Mensagens claras para fora da base e pergunta vazia; "Opção inválida." não diz quais opções são válidas. | 1 |
| 10. Ajuda e documentação | Não existe opção de ajuda nem exemplos de perguntas na interface; as instruções estão só no README. | 2 |

## Principais achados

**Pontos fortes:** transparência (fonte, data e aviso em toda resposta), recusa em inventar resposta fora da base, tratamento de entradas vazias, inválidas e ambíguas, e aviso de privacidade visível.

**Problemas mais graves (severidade 3):**
1. Ao navegar por tema, o usuário não vê as perguntas disponíveis e frequentemente recebe "sem resposta" (H6).
2. Termos populares como "RG" e perguntas de uma palavra ("cpf") não encontram orientações que existem na base (H2).

## Melhorias propostas

1. **Listar as perguntas do tema escolhido, numeradas**, para o usuário selecionar pelo número (resolve H6, H4 e parte de H2).
2. **Ampliar sinônimos** (`rg` → `identidade`/`cin`, `identidade antiga` etc.) e, para perguntas de uma palavra, sugerir as perguntas daquele assunto em vez de "sem resposta".
3. Melhorias menores: opção `V. Voltar`, opção `A. Ajuda` com exemplos, data em `dd/mm/aaaa`, esconder o tempo em ms do usuário final, mensagem de opção inválida indicando as opções válidas.

## Limitações

A avaliação heurística identifica problemas com base em princípios conhecidos, mas não mede a experiência de pessoas reais. Recomenda-se, como próximo passo, um teste com participantes do público-alvo usando as mesmas tarefas.
