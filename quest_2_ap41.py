h = float(input('Digite a altura: '))
s = str(input('Qual é o sexo (m ou f): '))
if s == 'm' or s == 'f': 
   if s == 'm':
      altmasc = (72.7*h)-58 
      print(f'O peso ideal é {altmasc: .2f}')
   if s == 'f':
      altfem = (62.1*h) - 44.7
      print(f'O peso ideal é {altfem: .2f}')
else:    
   print('Tente denovo')