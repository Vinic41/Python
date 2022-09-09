def avaliaApresentacao(x):
    dificuldade = float(input(". Grau de dificuldade: "))
    qtd = 1
    nota2 = 0
    while qtd <= x:
        nota = float(input(f". Nota do juíz {qtd}: "))
        nota2 = nota2+nota
        qtd = qtd+1
    nota2 = nota2*dificuldade
    return nota2


apre = float(input("Defina a quantidade de apresentações: "))
juiz = float(input("Defina a quantidade de juízes: "))
cont = 1
while cont <= apre:
    print(f'. Apresentação: {cont}')
    notatot = avaliaApresentacao(juiz)
    print(f'. Pontuação da apresentação: {notatot:.2f}')
    cont = cont+1
