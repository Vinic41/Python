pes=float(input('Digite seu peso (em kg): '))
alt=float(input('Digite sua altura (em metros): '))
circ=float(input('Digite a circunferência do seu quadril (em cm): '))
imc= pes/alt**2
iac= (circ/alt**1.5)-18
print (f'IMC = {imc:.3f}')
print (f'IAC = {iac:.3f}')
