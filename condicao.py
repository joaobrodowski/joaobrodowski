
nnome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
if idade <= 12:
    print("Resultado: Você é uma criança")
elif 12 < idade <= 18:
    print("Resultado: Você é um adolescente")
else:
    print("Resultado: Você é um adulto")
