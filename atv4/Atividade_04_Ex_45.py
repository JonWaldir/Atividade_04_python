# Decoração de varáveis
cima = 1
baixo = 1
soma = 0
# inicio

for cima in range(1,16,1):
    baixo = cima * cima
    if cima%2==0:
        soma = soma - (cima/baixo)
    else:
        soma = soma + (cima/baixo)
print(soma)
print(cima)
print(baixo)

# fim