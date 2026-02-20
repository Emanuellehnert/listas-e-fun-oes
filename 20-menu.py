numeros = []

def adicionar():
    try:
        n = float(input("Digite o número para adicionar: "))
        numeros.append(n)
        print(" Número adicionado!")
    except ValueError:
        print(" Erro: Digite um número válido.")

def mostrar():
    if not numeros:
        print(" A lista está vazia.")
    else:
        print(f" Lista atual: {numeros}")

def calcular_media():
    if not numeros:
        print(" Não há números para calcular a média.")
    else:
        media = sum(numeros) / len(numeros)
        print(f" A média dos números é: {media}")

while True:
    print("\n MENU DE NÚMEROS ")
    print("1. Adicionar número")
    print("2. Mostrar lista")
    print("3. Calcular média")
    print("4. Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        adicionar()
    elif opcao == '2':
        mostrar()
    elif opcao == '3':
        calcular_media()
    elif opcao == '4':
        print("Saindo do programa... Até logo!")
        break
    else:
        print(" Opção inválida!")