numeros = []

for i in range (5):
    num = int(input(f"Digite o {i+1}º numero:"))
    numeros.append(num) 

soma_total = sum(numeros)
print(f"A soma total de todos os números é: {soma_total}")