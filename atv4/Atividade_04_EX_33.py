#Declaração de variaveis
i  = 0
soma = 0
n = 0
#Inicio
n = int(input('Digite um numero para a sequencia  '))
for i in range(1,n+1,1):
    soma = soma + (1/i)
    print('o resultado:', soma)

#fim