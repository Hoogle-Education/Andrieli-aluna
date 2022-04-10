
p = int(input('digite a posição da porta P: '))
r = int(input('digite a posição da porta R: '))

if p == 0 :
  print('A bolinha caiu na saída C')
elif p == 1 and r == 0 :
  print('A bolinha caiu na saída B')
else:
  print('A bolinha caiu na saída A')