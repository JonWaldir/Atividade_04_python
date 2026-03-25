#Declaração de variáveis
dado1 = 1
dado2 = 1
deu7 = 0
#incio

for dado1 in range(1,7,1):
    for dado2 in range(1,7,1):
        if (dado1 + dado2==7):
            deu7 +=1
print(deu7)

# fim