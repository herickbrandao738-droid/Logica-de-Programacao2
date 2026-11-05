#9-	Crie um programa de adivinhação em que o computador escolhe aleatoriamente um número entre 1 e 50, 
# e o usuário precisa adivinhar. O programa deve fornecer feedback (maior ou menor) 
# a cada tentativa e permitir apenas 5 tentativas para acertar. Se o usuário acertar antes do limite, 
# exiba uma mensagem de vitória; caso contrário, revele o número ao final.
import random
numMaquina = random.randint(1,50)
num = 0
for i in range (1, 6):
    num = int(input("Tenta adivinhar o número!: "))
    if num == numMaquina:
        print ("Você acertou o número! O número era: " , numMaquina)
        break
    elif num < numMaquina:
        print ("número menor que o número sorteado. ")
    else:
        print ("número maior que o número sorteado. ")
print ("O número era: " , numMaquina)