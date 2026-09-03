import csv
import os


pasta_modulo06 = os.path.dirname(os.path.abspath(__file__))
pasta_meus_arquivos = os.path.join(pasta_modulo06, "meus_arquivos")

if not os.path.exists(pasta_meus_arquivos):
    os.makedirs(pasta_meus_arquivos)

caminho_arquivo = os.path.join(pasta_meus_arquivos, "notas_alunos.csv")

campos = ["Aluno", "Materia", "Nota"]
notas = [
    {"Aluno": "Ivan Silva", "Materia": "Matemática", "Nota": 9.5},
    {"Aluno": "Beatriz Vitoria", "Materia": "Português", "Nota": 10.0},
    {"Aluno": "Eric Renan", "Materia": "Educação Física", "Nota": 8.5},
]

with open(caminho_arquivo, "w", newline="", encoding="utf-8-sig") as arquivo:
    escritor = csv.DictWriter(arquivo, fieldnames=campos)
    escritor.writeheader()
    escritor.writerows(notas)

print("✓ Arquivo 'notas_alunos.csv' salvo em: modulo06/meus_arquivos/\n")


print("--- Lendo o arquivo CSV de Notas ---")
with open(caminho_arquivo, "r", encoding="utf-8-sig") as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        print(
            f"Aluno: {linha['Aluno']} | Matéria: {linha['Materia']} | Nota: {linha['Nota']}"
        )