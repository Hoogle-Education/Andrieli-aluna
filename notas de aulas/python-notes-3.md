# Estruturas de Repetição

## 1. `while` - *Enquanto*

Vai proporcionar um `if` durável que ao invés de checar se algo **é verdade**, checa **enquanto for verdade**.

 ```
 while <condição> :
  <código>
 ```

Fica implicito, mas é importante que sejam passados os seguintes 3 elementos para uma estrutura de repetição:

1. inicialização
2. verificação
3. atualização

```py
estoque = 10

while estoque != 0 :
  if estoque > 0 : 
    print('vendendo items')
    estoque -= 1 // estoque = estoque - 1
  else :
    print('comprando items')
    estoque += 1
```

## 2. keywords

### 2.1 break

Interrompe o laço e a estrutura de repetição no ponto em que foi mencionada.

```py
while True :

  if estoque == 0 : 
    break

```

### 2.2 continue

Pula o laço de repetição, mas não quebra o loop, e continua a partir do próximo laço.

```py
while True :

  pressao += 1

  if pressao > 10:
    print('desligando por segurança')
    break

  if pressao < 5 or pressao > 7:
    print('pressao fora do intervalo ideal')
    continue

  print('reação acontecendo')
```

# 3. for - *para*

o `for` fornece uma iteração mais dinâmica para o array, lista ou tupla em questão, além de já compactar todas as etapas necessárias durante a criação de uma estrutura de repetição

```py
for <iterator> in <array, list, tuple, str>:
  // código
```

## keyword `range()`

sintaxe:

> `range(stop)`

> `range(start, stop)`

> `range(start, stop, step)`

```py
for iterator in range(start, stop, step) :
  # faça algo
```

Analogo:
```py
int iterator = start

while iterator < stop :
  # faço algo
  iterator += step
```