def ler_inteiro(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor 
        except ValueError:
            print("Erro: Por favor, digite um número inteiro válido.")


num = ler_inteiro("Digite um número: ")
print(f"Você digitou o número: {num}")