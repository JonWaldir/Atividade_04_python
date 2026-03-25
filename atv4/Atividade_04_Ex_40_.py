#Declaração de variáveis
n1 = 0
n2 = 0
maior = 0
menor = 0
cta = 0 
div = 0
aux = 0
#inicio

n1 = int(input('Digite o n1: '))
n2 = int(input('Digite o n2 : '))
if n1 == n2:
    print('São iguais')
elif n1 > n2:
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1
for cta in range(menor+1,maior,1):
    div = 0
    for aux in range(1,cta+1,1):

        if cta % aux == 0:
         div = div + 1
    if div ==2:
        print(cta)


# fim