from math import trunc, ceil
tp = int(input('Tipo de ladrilho (1 ou 2):'))
if tp == 1 or tp == 2: 
    are = float(input('Área da sala: '))
    if tp == 1:
        qtlad80 = are/80 
        qtlad802 = ceil(qtlad80)
        print(f'Quantidade de ladrilhos: {qtlad802}')
    if tp == 2:
        qtlad60 = are/60 
        qtlad602 = ceil(qtlad60)
        print(f'Quantidade de ladrilhos: {qtlad602}')        