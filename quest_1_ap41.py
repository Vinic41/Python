
a = int(input('Cateto 1 (a): '))
b = int(input('Cateto 2 (b): '))
c = int(input('Hipotenusa (c): '))
cat = a**2 + b**2
hip = c**2
if cat == hip :
    print(f'{a: d}, {b:d}, {c:d} representam um terno pitagórico')
else :
    print(f'{a:d}, {b:d}, {c:d} NÃO representam um terno pitagórico')