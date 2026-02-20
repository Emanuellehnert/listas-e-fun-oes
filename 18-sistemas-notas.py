def ler_notas():

    notas = []
    for i in range(4):
        while True:
            try:
                n = float(input(f"Digite a {i+1}ª nota: "))
                if 0 <= n <= 10:
                    notas.append(n)
                    break
                else:
                    print("Nota inválida! Digite um valor entre 0 e 10.")
            except ValueError:
                print("Entrada inválida! Digite apenas números.")
    return notas

def calcular_media(lista_notas):
    
    return sum(lista_notas) / len(lista_notas)

def mostrar_resultado(media):
    
    print(f"\nMédia Final: {media:.2f}")
    if media >= 7:
        print("Situação: APROVADO! ")
    elif media >= 5:
        print("Situação: RECUPERAÇÃO. ")
    else:
        print("Situação: REPROVADO. ")

print("--- SISTEMA ESCOLAR ---")
minhas_notas = ler_notas()
media_final = calcular_media(minhas_notas)
mostrar_resultado(media_final)