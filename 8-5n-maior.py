numeros = []

for i in range (5):
    num = int(input(f"Digite o {i+1}º numero:"))
    numeros.append(num)
maior_numero = max(numeros)
print(f"O maior numero é: {maior_numero}")