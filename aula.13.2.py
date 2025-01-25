import random
from time import sleep

n1 = random.randint(0, 100)
tentativas = 0
tempo_restante = 30

print("Tens 30 segundos para adivinhar o número!")

while tempo_restante > 0:
    n2 = int(input("Escolhi um número de 0 a 100, tenta adivinhar qual é: "))
    tentativas += 1

    if n1 < n2:
        print("O número que escolheste é maior que o escolhido, tenta outra vez.")
    elif n1 > n2:
        print("O número que escolheste é menor que o escolhido, tenta outra vez.")
    else:
        print(f"Acertaste!!! Parabéns!!! Acertaste em {tentativas} tentativas!!!")
        break

    sleep(1)  # Pausa de 1 segundo
    tempo_restante -= 1
    print(f"Tempo restante: {tempo_restante} segundos")

if tempo_restante == 0:
    print("\nTempo esgotado! Não conseguiste adivinhar o número a tempo.")