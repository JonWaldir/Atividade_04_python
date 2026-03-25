#Declaração de variáveis
#  10 11 13 15 17 19 20
n1 = 0
n2 = 0
cta = 0
result = 0
maior = 0
menor = 0
#inicio
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
if n1 == n2:
    print('São números iguais')
elif n1 > n2:
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1
for cta  in range((menor + 1),maior ,1):
    if cta % 2 !=0:
        result_antigo = result
        result += cta
        print(f'{result_antigo} + {cta} = {result}')
print(result)
    
#FIM
        