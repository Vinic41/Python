pes= float(input('Digite seu peso (em kg): '))
alt=float(input('Digite sua altura (em metros): '))
sex=input('Seu sexo é masculino (M) ou feminino (F)? ')
imc = pes/ alt ** 2
if sex == 'M':
    if imc>25:
        pesid= 25 * alt ** 2
        print(f'Você deve perder {pes - pesid : .2f}kg para ter IMC = 25')
    else:
        print('Você não precisa perder peso para ter IMC <= 25')   
elif sex == 'F':
    if imc>24:
        pesid= 24 * alt ** 2
        print(f'Você deve perder {pes - pesid : .2f}kg para ter IMC = 24')
    else:
        print('Você não precisa perder peso para ter IMC <= 24')
else:
    print('A entrada contém dados não reconhecidos')       
    
