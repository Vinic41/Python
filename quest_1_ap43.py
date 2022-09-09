mm= float(input('Média móvel dos últimos 14 dias: ')) 
som= int(input('Somatório dos casos dos últimos 6 dias: '))
cas= int(input('Quantidade de casos de hoje: ')) 
mm7= (som + cas) / 7
dif = mm7 - mm
difper= (dif/mm)*100
if difper < 0:
   print(f'Casos diminuindo em {difper: .2f}%')
elif difper<= 15:
    print(f'Casos estáveis em {difper: .2f}%')
else:
    print(f'Casos aumentando em {difper: .2f}%')
