numeros = []

for i in range(5):
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

maior_numero = numeros[0]
for i in numeros:
    if i > maior_numero:
        maior_numero = i

print(f"O maior número digitado foi: {maior_numero}")