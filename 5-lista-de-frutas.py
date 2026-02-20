frutas = []

for i in range(5):
    fru = str(input(f"Digite a {i+1}º fruta: "))
    frutas.append(fru) 

fru = str(input("Digite a fruta que deseja romover: "))
frutas.remove(fru)
print("lista atualizada", frutas)
    

