import math

def impostoRenda(A):
    if A <= 1500:
        red = 0
        print('(-)IR: R$ 0.00')
    elif A <= 2500:
        red = A / 20
        print(f'(-)IR: R$ {red:.2f}')
    elif A <= 4500:
        red = A / 10
        print(f'(-)IR: R$ {red:.2f}')
    else:
        red = A / 5
        print(f'(-)IR: R$ {red:.2f}')
    return round(red, 2)




A = float(input('Digite o salário bruto: '))
y = impostoRenda(A)

inss = A / 10
print(f'(-)INSS: R$ {inss:.2f}')
fgts = A * 0.11
print(f'FGTS: R$ {fgts:.2f}')
if A <= 1500:
    print(f'Total de descontos: R$ {inss:.2f}')
elif A <= 2500:
     p = A / 20
     print(f'Total de descontos: R$ {inss+y:.2f}')
elif A <= 4500:
    p = A / 10
    print(f'Total de descontos: R$ {inss+y:.2f}')
else:
    p = A / 5
    print(f'Total de descontos: R$ {inss+y:.2f}')  
    
sl = A - y - inss
print(f'Salário Líquido: R$ {sl:.2f}')