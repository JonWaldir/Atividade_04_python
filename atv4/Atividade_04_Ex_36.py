#Declaração de variáveis
cta = 0
fat = 1
result = 0
n1 = 0
#inicio
n1 = int(input('Digite ate onde voce que ver a sequencia: '))

for cta in range(1,n1+1,1):
    fat = fat * cta
    print(fat)
    result = result + (1/fat)
    print(f'o resultado = {result}')
#fim