pressao = 0

while True :

  pressao += 1

  if pressao > 10:
    print('desligando por segurança')
    break

  if pressao < 5 or pressao > 7:
    print('pressao fora do intervalo ideal')
    continue

  print('reação acontecendo')

print('fim do programa')