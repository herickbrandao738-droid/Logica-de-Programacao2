#2-	Fazer um programa que calcule a tabuada de qualquer número, 
# e o limite de cálculo deve ser definido pelo usuário:

tabuada = int(input("Digite o número que você quer saber a tabuada: "))
num1 = int(input("Digite o número de até quanto você quer saber na tabuada: "))

for contador in range (1, num1 + 1):
    resultado = tabuada * contador
    print (tabuada, "X" , contador , "=" , resultado)
    