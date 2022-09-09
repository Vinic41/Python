def calculaJ(C, m):
    if C > 10000:
        t = 0.07
        J = C*t*m
    else:
        t = 0.1
        J = C*t*m
    if t == 0.1:
        t = 10
    else:
        t = 7
    return J, t


t = float(input('Capital Total para empréstimo: '))
i = t
while i > 0:
    c = float(input('Capital emprestado: '))
    emprest = i-c
    if emprest < 0:
        print(f' Empréstimo negado, capital total é de R$ {i:.2f}')
    i = i-c
    m = int(input('Quantidade de meses para quitação: '))
    juros, t = calculaJ(c, m)
    print(f' Taxa de juros aplicada:{t:d}%')
    print(f' Juros devido:{juros:.2f}')
    print(f' Valor total: {c+juros:.2f}')
    


# Capital emprestado:
