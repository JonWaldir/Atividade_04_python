#Declaração de variáveis
result = 0
cta = 0
tabuada = 0
#Inicio
tabuada = int(input('Digite o numero que voce quer ver a tabuada: '))
for cta in range(1,11,1):
    result = (cta * tabuada)
    print(f'{cta} X {tabuada} = {result}')

#Fim


