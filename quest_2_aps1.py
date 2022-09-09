def desconto(x, y):
    porc = 0
    if y == 'Pão de queijo':
        if x <= 50:
            porc = 10
            x = x*0.9
        elif x <= 100 and x > 50:
            porc = 12
            x = x*0.88
        else:
            porc = 15
            x = x*0.85
    elif y == 'Pastel de angu':
        if x <= 50:
            porc = 9
            x = x*0.91
        elif x <= 100 and x > 50:
            porc = 10
            x = x*0.9
        else:
            porc = 11
            x = x*0.89
    return x, porc


cont = 1
while cont > 0:
    nome = input("Informe o nome do produto: ")
    if nome == 'fim':
        cont = 0
    else:
     valor = float(input("Valor do pedido: R$ "))
     if valor > 0:
        desc, porc = desconto(valor, nome)
        print(f'Percentual de desconto: {porc:.2f}%')
        print(f'Valor com desconto: R$ {desc:.2f}')
