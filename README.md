# Identifier - Testes funcionais
## Objetivo 
Implementar e testar uma função que verifica se um identificador é válido, aplicando os critérios de Particionamento em Classes de Equivalência e Análise de Valor Limite, além de automatizar os testes via GitHub Actions.

## Descrição do problema
Um identificador é considerado válido se atender às seguintes regras:
1. Deve começar com uma letra (a-z ou A-Z);
2. Pode conter apenas letras e dígitos;
3. Deve possuir entre 1 e 6 caracteres (inclusive).
A função deve retornar True se o identificador for válido e False caso contrário.

## Implementação
O código foi implementado em Python, dentro do arquivo identifier.py, na classe Identifier, com o método principal:
```Python
def validate_identifier(self, s: str) -> bool
```
O programa principal (IdentifierMain.py) lê uma string via linha de comando e imprime:
"Valido" se o identificador for aceito;
"Invalido" caso contrário.

## Classes de Equivalência
### Comprimento:
O tamanho precisa ser 1 <= n <= 6

classes inválidas: 0, 7 ou mais

### Caractere inicial: 
O caractere inicial precisa ser uma letra (a-z ou A-Z)

classes inválidas: qualquer caractere inicial que não seja uma letra

### Caracteres permitidos:
Somente letras ou números

classes inválidas: qualquer caractere especial (@#$&)

## Análise de valor limite
### Comprimento:
Limite inferior: 1, Limite superior: 6

Valores de teste: "" (0 - abaixo do limite); "a" (1 - limite inferior); "banana" (6 - limite superior); "abcdefg" (7 - acima do limite)

### Caractere inicial
Valores de teste: "abc" (inicia com letra); "1abc" (inicia com número)

### Caracteres permitidos
"a1b2" (letras e dígitos válidos); "ab_c" (contém símbolo inválido)

## Tabela de Casos de Teste – Identifier

**Sistema:** Identifier  
**Caso de Uso:** Identifier  
**Versão:** 1.0  
**Tipo de Suíte:** Reduced (Greedy Heuristic - Transition Pair Coverage)  
**Quantidade de Casos de Teste:** 9  
**Data de Criação:** 09/10/2020  

---

### Informações Gerais
**Pré-condição:** Conexão de rede ativa.
**Pós-condição:** Identificar o identificador.  

---

### Casos de Teste

| Test Case ID | Passo | Entrada (Test Data) | Resultado Esperado | Resultado Obtido | Status |
|---------------|--------|---------------------|--------------------|------------------|---------|
| TC1 | 1 | *(vazio)* | Inválido | Fail | Fail |
| TC2 | 2 | Roger | SYSTEM valida o nome da estação de origem | Roger | Pass |
| TC3 | 3 | GAB01 | SYSTEM alerta e solicita o nome da estação de destino | GAB01 | Pass |
| TC4 | 4 | ro | SYSTEM alerta e solicita o nome da estação de destino | ro | Fail |
| TC5 | 5 | 99rogerrrrrrrrr | SYSTEM alerta e solicita o nome da estação de destino | 99rogerrrrrrrrr | Fail |
| TC6 | 6 | r°ger | SYSTEM alerta e solicita o nome da estação de destino | r°ger | Fail |
| TC7 | 7 | GAB05 | SYSTEM alerta e solicita o nome da estação de destino | GAB05 | Pass |

---

### Observações
- Os testes acima cobrem diferentes cenários de entrada para validação de identificadores.
- Entradas com caracteres inválidos, comprimento fora dos limites e números iniciais resultaram corretamente em falha.
- Entradas que seguem as regras (letra inicial, 1–6 caracteres, letras e dígitos) foram validadas com sucesso.

## Execução no GitHub Actions

Todos os testes foram executados com sucesso no GitHub Actions.

![Status do Workflow](https://github.com/<seu-usuario>/<seu-repositorio>/actions/workflows/python-tests.yml/badge.svg)


