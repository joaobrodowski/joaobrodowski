import time

# Função para exibir as opções do sistema
def exibir_menu():
    print("\n--- Sistema de Atendimento ao Cliente ---")
    print("1. Dúvidas")
    print("2. Reclamações")
    print("3. Sugestões")
    print("4. Sair")

# Função para simular o envio de uma dúvida
def atendimento_duvida():
    print("\nVocê escolheu: Dúvidas")
    print("Por favor, descreva sua dúvida:")
    duvida = input("Digite aqui: ")
    print(f"\nA sua dúvida: '{duvida}' foi registrada. Nossa equipe irá responder em breve!")
    time.sleep(2)
    print("Obrigado por entrar em contato conosco!")

# Função para simular o envio de uma reclamação
def atendimento_reclamacao():
    print("\nVocê escolheu: Reclamações")
    print("Por favor, descreva sua reclamação:")
    reclamacao = input("Digite aqui: ")
    print(f"\nA sua reclamação: '{reclamacao}' foi registrada. Pedimos desculpas pela inconveniência!")
    time.sleep(2)
    print("Nosso time está trabalhando para resolver isso o mais rápido possível!")

# Função para simular o envio de uma sugestão
def atendimento_sugestao():
    print("\nVocê escolheu: Sugestões")
    print("Por favor, descreva sua sugestão:")
    sugestao = input("Digite aqui: ")
    print(f"\nA sua sugestão: '{sugestao}' foi registrada. Agradecemos pela sua contribuição!")
    time.sleep(2)
    print("Sempre buscamos melhorar nossos serviços!")

# Função principal que gerencia o atendimento
def sistema_atendimento():
    while True:
        exibir_menu()
        try:
            opcao = int(input("\nEscolha uma opção (1-4): "))
            if opcao == 1:
                atendimento_duvida()
            elif opcao == 2:
                atendimento_reclamacao()
            elif opcao == 3:
                atendimento_sugestao()
            elif opcao == 4:
                print("Obrigado por utilizar o nosso sistema de atendimento! Até logo!")
                break
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")
        except ValueError:
            print("Por favor, insira um número válido.")

# Rodar o sistema
if __name__ == "__main__":
    sistema_atendimento()
