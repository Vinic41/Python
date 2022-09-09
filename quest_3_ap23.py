import math
fio=float(input('Forneça o comprimento do fio: '))
pes=float(input('Forneça a força peso: '))
mas=float(input('Forneça a massa: '))
g = pes/mas
t = 2*3.14 * math.sqrt(fio/g) 
print (f'A aceleração da gravidade é {g:.3f}')
print (f' O período do pêndulo é {t:.3f}')