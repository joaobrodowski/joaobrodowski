import random
def adivinhar_numero():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    print("Bem-vindo ao jogo de adivinhação!")
    print("Eu pensei em um número entre 1 e 100. Tente adivinhar qual é!")
    while True:
        try:
            palpite = int(input("Digite seu palpite: "))
        except ValueError:
            print("Por favor, digite um número válido.")
            continue
        tentativas += 1
        if palpite < numero_secreto:
            print("O número secreto é maior! Tente novamente.")
        elif palpite > numero_secreto:
            print("O número secreto é menor! Tente novamente.")
        else:
            print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
            break
adivinhar_numero()
