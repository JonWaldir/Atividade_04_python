# Declaração de variáveis
cta = 0
casa = 0
result = 1
soma = 0
#inicio
while True:
    casa = int(input('Digite uma casa entre 1 e 64 : '))
    if 0 <= casa <=64:
        break
    print('Voce digitou uma casa incorreta !')

for cta in range(0,casa + 1,1):
    soma += result
    result = result * 2
print(f"O RESULTADO FOI = {soma}")
# fim
