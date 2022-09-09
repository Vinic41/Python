cap=float(input('Capital emprestado:')) 
tpm= int(input('Quantidade de meses para quitação:')) 
jur = 0
if cap <= 10000 :
    jur = 0.1
    juros= cap * jur * tpm
    jurosapli = juros + cap
    print(f'Taxa de juros aplicada: 10%')
    print(f'Juros devido: {juros: .2f}')
    print(f'Valor total: {jurosapli: .2f}')
else:
    jur = 0.07
    juros= cap * jur * tpm
    jurosapli = juros + cap
    print(f'Taxa de juros aplicada: 7%')
    print(f'Juros devido: {juros: .2f}')
    print(f'Valor total: {jurosapli: .2f}') 
    
