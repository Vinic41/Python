ae = int(input('Anos de experiência: '))
lp = int(input('Linguagens de programação: '))
p = int(input('Projetos: '))
if ae >= 10 and lp >= 5 and p >= 10:
    print('Concorrendo à Vaga Sênior')
elif ae >= 3 and lp >= 3 and p >= 5:
    print('Concorrendo à Vaga Pleno. Para concorrer à Vaga Sênior, faltam:')
    if ae < 10:
        print(f'- {10-ae} anos de experiência')
    elif lp < 5:
        print(f'- {5-lp} linguagens de programação')
    else:
        p < 10
        print(f'- {10-p} projetos')
else:
    print('Concorrendo à Vaga Júnior. Para concorrer à Vaga Pleno, faltam:')
    if ae < 3:
        print(f'- {3-ae} anos de experiência')
    elif lp < 3:
        print(f'- {3-lp} linguagens de programação')
    else:
        p < 5
        print(f'- {5-p} projetos')
