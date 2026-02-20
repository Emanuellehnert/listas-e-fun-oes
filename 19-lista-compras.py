carrinho = []

def adicionar_item():
    item = input("O que deseja adicionar? ")
    carrinho.append(item)
    print(f" '{item}' adicionado com sucesso!")

def remover_item():
    exibir_lista()
    if carrinho:
        item = input("Qual item deseja remover? ")
        if item in carrinho:
            carrinho.remove(item)
            print(f" '{item}' removido!")
        else:
            print(" Item não encontrado na lista.")

def exibir_lista():
    print("\n--- SUA LISTA DE COMPRAS ---")
    if not carrinho:
        print("A lista está vazia.")
    else:
        for i, item in enumerate(carrinho, 1):
            print(f"{i}. {item}")
    print("-" * 28)


adicionar_item()
adicionar_item()
exibir_lista()
remover_item()
exibir_lista()