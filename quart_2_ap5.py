def converteMedidas(m):
    FT=0.3048*m
    FT=round(FT, 3)
    YD=0.9144*m
    YD=round(YD, 3)
    return FT,YD
print(f'Percurso 1: ')
m=float(input(f'  - Tamanho em metros: '))
FT,YD=converteMedidas(m)
print(f'  - Tamanho em pés...: {FT:.2f}')
print(f'  - Tamanho em jardas: {YD:.2f}')
print(f'Percurso 2: ')
m=float(input(f'  - Tamanho em metros: '))
FT,YD=converteMedidas(m)
print(f'  - Tamanho em pés...: {FT:.2f}')
print(f'  - Tamanho em jardas: {YD:.2f}')
print(f'Percurso 3: ')
m=float(input(f'  - Tamanho em metros: '))
FT,YD=converteMedidas(m)
print(f'  - Tamanho em pés...: {FT:.2f}')
print(f'  - Tamanho em jardas: {YD:.2f}')