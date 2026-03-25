#Declaração de variáveis 
cta = 0
num = 0
maior = 0
menor = 0

#inicio
for cta in range(1,6,1):
    num = float(input('Digite somente números positivos:'))
    while num < 0:
        print('Somente números positivos! ')
        num = float(input('Digite somente números positivos:'))
        
    
    if cta ==1:
        menor = num
        maior = num
    else:
        if num > maior :
            maior = num
        if num < menor:
            menor = num
print(f'O maior numero foi : {maior} e o menor {menor}')
        

    