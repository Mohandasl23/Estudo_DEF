# Guia de Estudo: Try e Except em Python

Este documento serve como um guia explicativo sobre o uso e a importância dos blocos `try` e `except` em Python, utilizando o código do projeto `cafeteria` como exemplo prático.

---

## 1. O que é o `try` e `except`?

O `try` (tentar) e `except` (exceção/tratar) é a estrutura básica utilizada no Python para **tratamento de erros (exceções)**. 

Imagine que ele funciona como uma **rede de segurança**: você diz ao Python para "tentar" executar uma parte do código e, caso ocorra um erro previsto, ele executa um "plano de contingência" em vez de travar o programa.

---

## 2. Por que usá-los?

* **Evitar travamentos (Crashes):** Sem o tratamento de erros, qualquer falha faz o programa fechar imediatamente, mostrando mensagens de erro técnicas e assustadoras para o usuário final.
* **Melhorar a Experiência do Usuário:** Permite que você substitua erros do sistema por mensagens amigáveis e explicativas (por exemplo, pedir para digitar apenas números).
* **Robustez do Sistema:** Garante que o programa continue rodando mesmo se alguma operação secundária falhar.

---

## 3. Estrutura Básica

```python
try:
    # Código "perigoso" que pode gerar algum erro inesperado
    numero = int(input("Digite um número: "))
except ValueError:
    # Código executado CASO ocorra especificamente o erro 'ValueError'
    print("O valor digitado não é um número válido!")
```

---

## 4. O Exemplo Prático da Cafeteria

No arquivo `def.py`, o bloco foi implementado para tratar o caso onde o usuário digita texto (como "dois") em vez de um número:

```python
def cafeteria():
    # ...
    try:
        # O input retorna texto. Se o usuário digitar letras, int() falhará.
        valor = int(input("Digite o numero da sua escolha: "))
        
        # ... (condições if/elif/else) ...
        
    except ValueError:
        # Se ocorrer uma falha de conversão numérica, esta mensagem é exibida
        print("\n-> Erro: Por favor, digite apenas numeros inteiros.")
```

### O que acontece nos bastidores:
1. O programa tenta converter a entrada do usuário em um número inteiro (`int()`).
2. Se o usuário digitar `3`, a conversão funciona, as condições `if/elif` são testadas, e o bloco `except` é pulado.
3. Se o usuário digitar `"dois"`, a conversão falha gerando um erro de valor (`ValueError`). O Python interrompe o bloco `try` imediatamente e executa as instruções dentro de `except ValueError`.

---

## 5. Quando você DEVE usar `try` e `except`?

Você deve utilizar essa estrutura sempre que o seu programa interagir com **fatores externos imprevisíveis**:

1. **Entradas do Usuário (`input`):** Quando o usuário pode digitar algo incorreto, fora do padrão ou em formato inesperado.
2. **Operações de Arquivos (I/O):** Ao tentar abrir, ler ou salvar arquivos que podem não existir ou estar bloqueados/corrompidos.
3. **Conexões de Internet e APIs:** Ao buscar dados de um site ou banco de dados remoto (a rede pode cair, o site pode estar fora do ar).
4. **Cálculos Matemáticos Específicos:** Situações onde pode ocorrer divisão por zero (`ZeroDivisionError`).

---

## 6. Boas Práticas

* **Seja Específico:** Evite usar um `except` genérico (sem especificar o tipo de erro, como apenas `except:`). Sempre especifique qual erro você quer capturar (ex: `except ValueError:`). Isso evita ocultar bugs de sintaxe ou lógica que você deveria corrigir no código.
* **Mantenha o bloco `try` curto:** Coloque dentro do `try` apenas as linhas de código que realmente podem gerar a exceção que você deseja tratar.
