#  6-	Peça ao usuário para fornecer um número inicial e um intervalo. 
# Em seguida, faça uma contagem regressiva do número inicial até zero, 
# decrementando pelo intervalo especificado.

num = int(input("Escreva o número para a contagem regressiva: "))
intervalo = int(input("Escreva o intervalo de tempo da contagem: "))
for i in range (num, -1 , -intervalo):
    print (i)