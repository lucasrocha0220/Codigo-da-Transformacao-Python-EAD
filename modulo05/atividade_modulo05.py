
def saudacao(nome):
    print(f"Olá, {nome}! Seja bem-vindo(a).")


def calcular_media(notas):
    media = sum(notas) / len(notas)
    if media >= 7:
        print(f"Média: {media:.2f} - Aprovado!")
    else:
        print(f"Média: {media:.2f} - Reprovado!")



def maior_menor(lista):
    maior = max(lista)
    menor = min(lista)
    return maior, menor




# Teste da Atividade 1
saudacao("Maria")
# Teste da Atividade 2
notas_aluno = [8.0, 7.5, 6.0]
calcular_media(notas_aluno)


numeros = [15, 3, 42, 8, 23]
maior, menor = maior_menor(numeros)
print(f"Maior valor: {maior} | Menor valor: {menor}")