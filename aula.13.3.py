import random
v_joagadorA = 100
v_joagadorB = 100
while True:
    soco = random.randint(0, 10)
    v_joagadorB -= soco
    print(f"======================================================================\n"
          f"Jogador B levou um soco de {soco} de dano. Vida restante: {v_joagadorB}\n"
          f"======================================================================\n")
    soco = random.randint(0, 10)
    v_joagadorA -= soco
    print(f"======================================================================\n"
          f"Jogador A levou um soco de {soco} de dano. Vida restante: {v_joagadorA}\n"
          f"======================================================================\n")
    if v_joagadorA <= 0 or v_joagadorB <= 0:
        break
if v_joagadorA <= 0:
    print("Jogador A foi derrotado!")
    print("Parabéns Jogador B!")
if v_joagadorB <= 0:
    print("Jogador B foi derrotado!")
    print("Parabéns Jogador A!")