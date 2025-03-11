import random
print("SEJA MUITO BEM VINDO AO JOGO DE ADIVINHAÇÃO")
print ("Tente adivinhar entre 1 e 10!!")
numerosecreto = random.randint(1,10)
palpite = int(input("Digite seu número de palpite:"))
while 

tentativas = 0 
max_tentativas = 3

if palpite < numerosecreto:
    print( "Muito baixo, tente novamente.")

elif palpite > numerosecreto:
    print("Muito alto, tente novamente.")

else:
    print("Parabens, Você acertou o número!")


