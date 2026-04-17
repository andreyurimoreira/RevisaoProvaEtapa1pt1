from ler import leitura
from menu import mostrar

print("Bem Vindo a PetShop")

print("O que vocce deseja fazer?")
opcao = input("""
        1- Dar banho
        2- Sair """)

match opcao: 
    case "1":
        dados = leitura()
        mostrar(dados)

        raca = input("digite a raca: ").lower()
        peso = dados[raca]

        valor = peso * 2.5

        print(f"O cachorro {raca}, peso {peso}kg")
        print(f"valor do banho: R${valor:.2f}")
    case "2":
            print("saindo")
    case _:
            print("essa opcao nao existe")        
 

