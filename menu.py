def mostrar(dados):
    print("Cachorros")
    for c, raca in enumerate(dados.keys(), start=1):
        print(f"{c} - {raca}")