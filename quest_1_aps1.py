def desconto(x):
    porc = 0
    if x<=250:
        porc = '3%'
        x=x*0.97
    elif x<=550 and x>250:
        porc = '6%'
        x= x*0.94
    elif x<=750 and x>550:
        porc = '8%'
        x=x*0.92
    else:
        porc = '10%'
        x=x*0.9
    return x,porc
    
valor = float(input("Defina o valor total da compra: R$ "))
if valor>0:
    desc,porc= desconto(valor)
    print(f'Desconto de {porc}.')
    print(f'Valor com desconto: R$ {desc:.2f}')
else:
    print('Erro: Valor total inválido.')