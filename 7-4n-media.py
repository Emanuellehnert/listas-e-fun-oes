numeros = []

for i in range (4):
    num = int(input(f"Digite o {i+1}º numero:"))
    numeros.append(num)

soma_total = 0 
for n in numeros: 
    soma_total += n 

media = soma_total / len(numeros) 

print(f"A sua média é igual á: {media}")