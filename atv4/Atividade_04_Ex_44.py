# Declaração de variáveis
base = 0
expoente = 0
pot = 1 
cta = 0
#inicio
base = int(input('Digite a base :'))
expoente = int(input('Digite o expoente:'))
for cta in range(1,expoente+1,1):
    pot = pot*base
    print(pot)

# fim