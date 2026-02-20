nomes = []

for i in range (3):
    nome = str(input(f"Digite o {i+1}º nome:"))
    nomes.append(nome)
print("\n --- Lista atualizada ---")

for nome in nomes: 
    print(f"- {nome}") 



