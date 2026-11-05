#5-	Escreva um algoritmo que calcule a média dos números digitados pelo usuário, 
# se eles forem pares. Termine a leitura se o usuário digitar zero (0)
qtdNum = 0
numerosPares = 0
while num > 0:
    num = float(input("Digite um número: "))
    if num == 0:
        break
    if num % 2 == 0 and num != 0:
        numerosPares += num
        qtdNum += 1
media = numerosPares/qtdNum
print ("A média dos seus números é: " , media)