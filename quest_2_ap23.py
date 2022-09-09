pt1=float(input('Informe a nota PT1: '))
ep1=float(input('Informe a nota EP1: '))
pt2=float(input('Informe a nota PT2: '))
ep2=float(input('Informe a nota EP2: '))
av1= pt1*0.3 + ep1*0.15
av2= pt2*0.4 + ep2*0.15
ns = av1 + av2
print (f' A nota na AV1 é: {av1:.2f}')
print (f' A nota na AV2 é: {av2:.2f}')
print (f' A nota no semestre é: {ns:.2f}')