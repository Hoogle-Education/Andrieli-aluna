estoque = int(input('digite o estoque: '))

while True :

  if estoque == 0 : 
    break
  
  if estoque > 0 : 
    print(f'vendendo items || estoque = {estoque}')
    estoque -= 1 # estoque = estoque - 1
  else:
    print(f'comprando items || estoque = {estoque}')
    estoque += 1