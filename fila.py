fila = [ ]
MAX_FILA = 10

def add_pessoa(pessoa):
    nome = input("Digite o nome da pessoa")
    if len(fila) < MAX_FILA:
        fila.append(pessoa)
        print(f"{nome} entrou na fila.")
    else:
        print("A fila está cheia. Não é possível adicionar mais pessoas.")

def chamada():
        pessoa = fila[0]
        fila.pop(0)
        print(f"{pessoa} saiu da fila.")

def ver_fila():
        print(f"Fila atual:", " -> ", "{fila}")

  
def menu():

    while True:
             print("\n1. Adicionar à fila")
             print("2. Remover da fila")
             print("3. Ver fila")
             print("4. Sair")
             opcao = input("Escolha uma opção: ")
   
             if opcao == "1":
                     add_pessoa()
             elif opcao == "2":
                     chamada()
             elif opcao == "3":
                     ver_fila()
             elif opcao == "4":
                     print("Saindo do programa...")
                     break
             else:
                     print("Opção inválida, tente novamente.")