#Declarção de variaveis 
fat = 0
c = 0
n = 0
#incio
fat = 1 
n = int(input('Digite um numero para fazer o fatoria: '))
for c in range(1,n+1,1):
    fat = fat * c
    print(fat)
    

#fim