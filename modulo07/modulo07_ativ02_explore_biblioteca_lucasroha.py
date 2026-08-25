def sistema_avaliador():
    print("=== SISTEMA DE AVALIAÇÃO ===")
    
    # Nome do objeto, produto ou serviço avaliado
    item = input("Digite o que está sendo avaliado (ex: Produto, Atendimento): ").strip()
    
    # Quantidade de critérios
    while True:
        try:
            qtd_criterios = int(input("Quantos critérios deseja avaliar? "))
            if qtd_criterios > 0:
                break
            print("Digite um número maior que zero.")
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")

    avaliacoes = {}
    
    # Coleta de notas para cada critério
    for i in range(1, qtd_criterios + 1):
        criterio = input(f"\nNome do {i}º critério: ").strip()
        while True:
            try:
                nota = float(input(f"Nota para '{criterio}' (0 a 10): "))
                if 0 <= nota <= 10:
                    avaliacoes[criterio] = nota
                    break
                else:
                    print("Por favor, digite uma nota de 0 a 10.")
            except ValueError:
                print("Entrada inválida! Digite apenas números.")

    # Processamento dos resultados
    media = sum(avaliacoes.values()) / len(avaliacoes)
    
    # Exibição do relatório
    print("\n" + "="*30)
    print(f" RELATÓRIO DE AVALIAÇÃO: {item.upper()}")
    print("="*30)
    for crit, nota in avaliacoes.items():
        print(f"• {crit}: {nota:.1f}")
    
    print("-" * 30)
    print(f"MÉDIA GERAL: {media:.1f}")
    
    # Classificação final
    if media >= 8.0:
        print("Classificação: EXCELENTE ⭐⭐⭐")
    elif media >= 6.0:
        print("Classificação: BOM ⭐⭐")
    elif media >= 4.0:
        print("Classificação: REGULAR ⭐")
    else:
        print("Classificação: INSATISFATÓRIO ❌")
    print("="*30)

if __name__ == "__main__":
    sistema_avaliador()
    