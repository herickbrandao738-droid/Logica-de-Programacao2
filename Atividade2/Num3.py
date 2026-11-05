##3-	Fazer um programa que retorne quantos valores digitados pelo usuário são negativos. 
# Repetir o enquanto até o usuário digitar o valor ZERO:

negativos = 0
while True:
    num = int(input("Digite um numero ai, e para desligar, digite 0: "))
    if num < 0:
        negativos += 1

    if num == 0:
        print ("A quantidade de números negativos digitados é: " , negativos)
        break