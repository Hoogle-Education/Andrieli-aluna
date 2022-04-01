# Introdução ao Python 🐍

## Princípio da saída - `print()`

Usamos o `print` com a mensagem desejada entre aspas.

```py
print('Hello World!')
```

O `print` também pode ser usado para mostrar variáveis.

```py
a = 2
print(a)
```

## Print com formatação de dados

Para melhorar a saída quando temos variáveis de vários tipos e queremos colocá-las em um print, podemos usar o modo `format` do `print`.

```py
var1 = 2
var2 = 4.5

print(f'O valor da variável 1 é {var1}')
print(f'O valor da variável 2 é {var2}')
```

# Tipos no **Python**

|Origem| keyword | Descrição |
|:-:|:-:|:-:|
|Inteiro| `int` | Um número inteiro |
|Real| `float`| Número com ponto flutuante |
|String | `str`| Coleção de caracteres |
| Booleano | `bool` | Guarda `True` ou `False` |

# Realizando entrada de dados

Usamos o comando `input()` para ler um dado e salvar numa variável.

```py
a = input()
b = input()

print(a+b)
```

⚠️ **Problema:** Desta forma ele apenas concatena as `str`'s lidas pelas variáveis a e b.

## Usando a `type()`

Podemos descobrir o tipo de uma variável, e desta forma veremos que o `input()` sempre puxa `str`'s por segurança. Possíveis erros:

> 1 + 1 = 11

Para evitar isso, faremos *boxing and unbonxing*.

Lendo as entradas como inteiros:
```py
a = int( input() ) 
b = int( input() ) 

print(a+b)
```
Desta forma, voltamos ao programa que soma dois números pois existe a conversão da entrada lida.

### Input messages

sintaxe:
```py
  input(message)
```

A `message` passada pela `input` é apresentada antes da input ser inserida.

Exemplo:
```py
frase = input('Digite uma frase: ')
print( f'você digitou: {frase}' )
```

# Estruturas de Seleção - `if-elif-else`

## Estrutura `if`

Testa uma condição e executa o código em seu escopo, se a condição for verdadeira.

O escopo de um `if` é todo o intervalo de linhas abaixo que estiver um `tab` atrás da chamada do `if`.

Sintaxe genérica:
```
if <condição> :  
  <seu_código_se_for_verdadeira_condição>
```

Exemplo:
```py
nota = 7.2

if nota > 7 :
  print('Aprovado')
```

## 2. Estrutura `if-else`

Sintaxe genérica:
```
if <condição> :  
  <seu_código_se_for_verdadeira_condição>
else :
  <seu_código_se_for_falsa_condição>
```
Exemplo:
```py
nota = 7.2

if nota > 7 :
  print('Aprovado')
else :
  print('Não aprovado')
```

## 3. Estrutura `if-elif-else`

```py

```
