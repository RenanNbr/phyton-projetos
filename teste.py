#numero = 10

#if numero > 5:
 #   print("O numero é maior que 5")

 ###################################################
#numero = 10

#if numero > 10:
   #  print("O numero é maior que 10.")
#elif numero == 10:
  #   print("o numero é exatamente 10.")
#elif numero < 10:
 #    print("O numero é menor que 10.")

##############################################
#numero1 = 89

##################
#nota = 85

#if nota >= 90:
 #   print("A")
#elif nota >= 80:
 #       print("B")
#elif nota >= 70:
   #     print("C")
#elif nota >= 60:
  #      print("D")
#else:
 #   print("F")

total_de_tentativas = 3
rodada = 1

import random

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random_element = random.choice(my_list)
print(f"Random element from the list: {random_element}")

print("########################")
print("Jogo de acertar o numero!")
print("########################")

while(rodada <= total_de_tentativas):

    print("tentativas",rodada,"de",total_de_tentativas)
    print("#################################")
    chute  =input("digite o seu numero =")

    print("voce digitou" ,chute)

    chute1 =int(chute)

    acertou = random_element == chute1
    maior = random_element < chute1
    menor = random_element > chute1


    if(acertou):
     print("")
     print("você acertou")
     print("")
     rodada = rodada + 4
    else:
     if (menor):
      print("")
      print("você errou! O numero é maior que o seu numero")
      print("")
      rodada = rodada + 1

     if(maior):
      print("")
      print("você errou! O numero é menor que o seu numero")
      print("")
      rodada = rodada + 1

else:
    print("FIM DE JOGO!")

