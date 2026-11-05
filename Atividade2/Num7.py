#7-	Crie um programa que solicite números ao usuário continuamente até que ele insira um número negativo. 
# Em seguida, exiba a média dos números positivos fornecidos.

mediaIdade = 0
contador = 0
idade = 0
idadeTotal = 0
while idade >= 0:
    idade = int(input("Escreva uma idade ai: "))
    if idade >= 0:
        contador += 1
        idadeTotal += idade
        mediaIdade = idadeTotal / contador
print ("A média das idade é: " , mediaIdade)