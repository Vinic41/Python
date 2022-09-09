import math
def minimo (fg,b):
    min=fg + (fg * b)
    return a

def maximo (hj,b):
    max = hj + (hj * b)
    return a

def calcDano (a,b,d):
    f = minimo(math.trunc(a * (1 + b) * (1 - d / (100 + d))))
    return f

def  vidaAposGolpe (v,a,b,d):
    x = maximo(v-calcDano(a,b,d))
    return x

b=0.15
a = int(input('Força de ataque do personagem 1: '))
f1 = maximo (a,b)
b=0
a = int(input('Força de ataque do personagem 2: '))
f2 = minimo (a,b)
b= 0
a = int(input('Força de ataque do personagem 3: '))
f3 = minimo (a,b)
b=0.15
a = int(input('Força de ataque do personagem 4: '))
f4 = maximo (a,b)
fg = f1 + f4
hj = f2 + f3
d = int(input('Força de defesa do inimigo: '))
c = calcDano (a,b,d) 
v = int(input('Vida inicial do inimigo: '))
va = vidaAposGolpe (v,a,b,d)
ve = va * -1
#ve = ve / 100000
ve = math.floor (ve)
r = v - ve
print(f'A vida do inimigo será: {r}')



va1 = vidaAposGolpe(v, calc2)
va2 = vidaAposGolpe(v, calc4)
va3 = vidaAposGolpe(v, calc6)
va4 = vidaAposGolpe(v, calc8)
vr = v - va1
vr2 = vr - va2
vr3 = vr2 - va3
vr4 = vr3 - va4
vr4 = math.floor(vr4)