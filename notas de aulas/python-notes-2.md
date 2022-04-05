# Estruturas de Seleção - `if-elif-else`

## Estrutura `if` - "Se ..."

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

## 2. Estrutura `if-else` - "Se..., Senão..."

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

```
if <condição> :  
  <seu_código_se_for_verdadeira_condição>
elif <condição2> :
  <seu_código_se_for_verdadeira_condição2>
else :
  <seu_código_se_for_falsa_condição>
```

```py
nota = 6.3
if nota >= 7 :
  print('Aprovado')
elif nota > 4 :
  print('recuperação')
else:
  print('reprovado')
```

## 4. Possíveis estruturas `if`
```
if -> else
if -> elif -> elif
if -> elif -> elif -> ... -> else
```

# Operadores lógicos 

## Comparações
|Operador|Simbologia|Exemplo|Descrição|
|:--:|:--:|:--:|:--:|
|Igualdade|`==`|`a==b`|Retorna `True` ou `False`, caso a seja igual a B|
|Maior igual|`>=`|`a>=b`|Retorna `True` ou `False`, caso a seja maior ou igual a B|
|Diferente|`!=`|`a!=b`|Retorna `True` ou `False`, caso a seja diferente de B| 

## Operações
|Operador|Simbologia|Exemplo|Descrição|
|:--:|:--:|:--:|:--:|
|Potência|`**`|`a**b`|A elevado a B|
|Resto/Mod|`%`|`a%b`|Retorna o resto de A divido por B|
|Soma reflexiva|`+=`|`a+=b`| `a = a + b` |
|Produto reflexiva|`*=`|`a*=b`| `a = a * b` |
|Divisão reflexiva|`/=`|`a/=b`| `a = a / b` |

## Operações entre condições

True and False = False
True and True = True

|Operador|Simbologia|Descrição|
|:--:|:--:|:--:|
|"e"|`&&`/`and`|Testa se ambas as condições serão verdade simultaneamente|

