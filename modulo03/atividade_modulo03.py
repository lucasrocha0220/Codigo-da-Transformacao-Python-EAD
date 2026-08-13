compras = {
    1: "Arroz",
    2: "Feijão",
    3: "Macarrão",
    4: "Açúcar",
    5: "Sal",
    6: "Café",
    7: "Leite",
    8: "Pão",
    9: "Manteiga",
    10: "Queijo",
    11: "Presunto",
    12: "Ovos",
    13: "Frango",
    14: "Carne",
    15: "Peixe",
    16: "Batata",
    17: "Tomate",
    18: "Cebola",
    19: "Alho",
    20: "Cenoura",
    21: "Alface",
    22: "Banana",
    23: "Maçã",
    24: "Laranja",
    25: "Limão",
    26: "Uva",
    27: "Melancia",
    28: "Sabonete",
    29: "Shampoo",
    30: "Condicionador",
    31: "Pasta de dente",
    32: "Escova de dente",
    33: "Papel higiênico",
    34: "Detergente",
    35: "Sabão em pó",
    36: "Amaciante",
    37: "Desinfetante",
    38: "Esponja",
    39: "Saco de lixo",
    40: "Papel toalha",
    41: "Guardanapo",
    42: "Água",
    43: "Suco",
    44: "Refrigerante",
    45: "Biscoito",
    46: "Chocolate",
    47: "Iogurte",
    48: "Farinha",
    49: "Óleo",
    50: "Vinagre"
}

while True:
    print("\n--- LISTA DE COMPRAS ---")
    print("1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Visualizar lista")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        item = input("Digite o item que deseja adicionar: ")

        novo_numero = max(compras.keys()) + 1
        compras[novo_numero] = item

        print("Item adicionado!")

    elif opcao == "2":
        numero = int(input("Digite o número do item que deseja remover: "))

        if numero in compras:
            del compras[numero]
            print("Item removido!")
        else:
            print("Item não encontrado.")

    elif opcao == "3":
        print("\nItens da lista:")

        for numero, item in compras.items():
            print(numero, "-", item)

    elif opcao == "4":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")