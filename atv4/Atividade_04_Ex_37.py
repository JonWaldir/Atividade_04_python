#Declaração de variáveis
termo1 = 1
termo2 = 1
proximo = 0
cta= 0
#inicio

for cta in range(1,1001,1):
    print(termo1)
    proximo = termo1 + termo2
    termo1 = termo2
    termo2 = proximo
