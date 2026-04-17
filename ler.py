import json 
def leitura():
    with open('dados.json','r', encoding='utf-8') as arquivo:
        dado = json.load(arquivo)
    return(dado)
    

dados = leitura()

for chave, valor in dados.items():
    print(chave, "e", valor)