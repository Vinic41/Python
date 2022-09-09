def verifica(n):
    i = 0
    z = 0
    perf= 1
    perf2=0
    while i < n:
        z= z+1
        div = n % z
        if div == 0:
            perf = n-i 
            perf2 = perf - n
        i = i+1
    return perf2

n = 1
while n > 0:
    n = int(input('Digite um número: '))
    perf = verifica(n)
    perf = perf * -1
    print(perf)
