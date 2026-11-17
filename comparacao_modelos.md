# Comparação reproduzível de dois modelos de resposta

Os modelos A e B são **formatadores determinísticos**, não chamadas a um LLM.
A: orientação e fonte. B: orientação, fonte, data de verificação, aviso e temas relacionados.

| Critério objetivo | Modelo A | Modelo B |
|---|---|---|
| Exibe orientação | Sim | Sim |
| Exibe fonte URL | Sim | Sim |
| Exibe data de verificação | Não | Sim |
| Exibe aviso de limitação | Não | Sim |
| Sugere temas relacionados | Não | Sim |

**Método:** usar `consultar(pergunta, base, modelo='A')` e `consultar(pergunta, base, modelo='B')` para uma mesma pergunta válida; comparar os campos apresentados. O modelo B foi selecionado por maior rastreabilidade e explicitação dos limites. Esta comparação estrutural não comprova preferência ou facilidade de leitura por pessoas: isso exigiria teste com usuários; a avaliação heurística em `docs/teste_usabilidade.md` analisa a interface com base em princípios, não em preferência medida.

**Exemplo:** `O que é uma conta GOV.BR?` — ambos exibem a orientação recuperada e a URL; somente B mostra data, aviso e assuntos relacionados. Não afirmar melhoria percentual de compreensão sem pesquisa com usuários.
