while True:

    def calcular_media(notas):
        media = sum(notas) / len(notas)

        print(f"\nSua média é: {media:.1f}")

        if media >= 7:
            print("Aprovado!")
        else:
            print("Reprovado!")


    nome = input("Digite seu nome: ")

    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    print(f"\nAluno: {nome}")

    calcular_media([nota1, nota2, nota3])

    print("\n--- Calculando novamente ---\n")