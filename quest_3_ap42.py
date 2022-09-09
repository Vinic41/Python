from math import sqrt, tan
q= int(input('Digite a quantidade de lados: '))
l=0
if q<3:
     print('Não é um polígono')
else:
  if q> 7:
     print('Polígono não identificado')
  else :
    
    
    if q>=3 and q<7:
     l=float(input('Digite a medida do lado:'))
     if q == 3:
        area = l**2 * sqrt(3)/4
        print(f'O polígono é um triângulo com área: {area: .2f}')
     if q == 4:
        area = (l**2)
        print(f'O polígono é um quadrado com área: {area: .2f}')
     if q == 5:
        area= 5 * l**2 / (4 * tan(0.6283))
        print(f'O polígono é um pentágono com área: {area: .2f}')
     if q == 6:
        area= (3*l**2 * sqrt(3))/2
        print(f'O polígono é um hexagono com área: {area: .2f}')


    

