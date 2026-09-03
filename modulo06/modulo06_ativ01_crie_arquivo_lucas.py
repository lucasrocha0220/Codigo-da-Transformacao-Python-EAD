import os


pasta_modulo06 = os.path.dirname(os.path.abspath(__file__))
pasta_meus_arquivos = os.path.join(pasta_modulo06, "meus_arquivos")


if not os.path.exists(pasta_meus_arquivos):
    os.makedirs(pasta_meus_arquivos)

caminho_arquivo = os.path.join(pasta_meus_arquivos, "dados_arquivo.txt")


conteudo = [
    "Ivan Silva;40 anos;02899-000;947541;ivanpaulino@mail.com\n",
    "Beatriz Vitoria;30 anos;057193-000;978786;beavitoria@mail.com\n",
    "Eric Renan;17 anos;089880-100;98799;ericrenan@gmail.com\n",
]


with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
    arquivo.writelines(conteudo)

print("✓ Arquivo 'dados_arquivo.txt' salvo em: modulo06/meus_arquivos/\n")


print("--- Lendo o conteúdo do arquivo TXT ---")
with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
    print(arquivo.read())