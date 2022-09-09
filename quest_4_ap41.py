n = input('Entre com o nome: ')
i = float(input('Entre com a idade: '))
s = str(input('Entre com o sexo (m ou f): '))
if s == 'm' or s == 'f': 
    if s == 'm':
      maiormasc = 18 - i  
      if maiormasc <= 0:
          print(f'{n} tem maioridade civil')
      else:
          print(f'Faltam {maiormasc: .1f} anos para {n} atingir a maioridade')
    if s == 'f':
      maiorfem = 21 - i
      if maiorfem <= 0:
          print(f'{n} tem maioridade civil')
      else:
          print(f'Faltam {maiorfem: .1f} anos para {n} atingir a maioridade')
else:    
   print('Tente denovo')