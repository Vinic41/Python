med= float(input('Média no semestre: ')) 
freq= int(input('Frequência no semestre: ')) 
if med<6 and freq>=75:
    print(' Conceito: exame especial')
    print(f'Justificativa: média { 6-med: .2f} abaixo da mínima')
elif freq<75:
     print(' Conceito: reprovado por faltas')
     print(f'Justificativa: frequência { 75-freq}% abaixo da mínima')
elif med >6 and freq>= 75:
    print(' Conceito: aprovado')

    