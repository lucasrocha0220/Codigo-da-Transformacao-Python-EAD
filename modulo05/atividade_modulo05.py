# 1. Função de saudação personalizada
def saudacao(nome):
    print(f"Olá, {nome}! Seja bem-vindo(a).")

# 2. Função para calcular média e verificar aprovação
def calcular_media(notas):
    media = sum(notas) / len(notas)
    print(f"Média: {media:.2f}")
    
    if media >= 7:
        print("Status: Aprovado!")
    else:
        print("Status: Reprovado!")

# 3. Função para retornar o maior e o menor valor
def maior_menor(numeros):
    maior = max(numeros)
    menor = min(numeros)
    return maior, menor


# --- Executando as três funções ---

# Teste da Função 1
nome_usuario = input("Digite seu nome: ")
saudacao(nome_usuario)
print("-" * 30)

# Teste da Função 2 (solicitando as notas ao usuário)
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

notas_aluno = [nota1, nota2, nota3]
calcular_media(notas_aluno)
print("-" * 30)

# Teste da Função 3
lista_numeros = [12, 5, 8, 42, 1, 19]
maior_val, menor_val = maior_menor(lista_numeros)
print(f"Maior valor: {maior_val} | Menor valor: {menor_val}")