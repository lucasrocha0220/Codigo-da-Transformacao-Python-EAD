"""
Solução alternativa.
Classificando idades: Use if-elif-else para criar um programa
que classifique a idade de uma pessoa em 
"Criança", "Adolescente", "Adulto" ou "Idoso".
"""


idade = int(input("Digite a sua idade: "))


if idade < 13:
    print("Você é uma Criança.")
elif idade < 18:
    print("Você é um Adolescente.")
elif idade < 60:
    print("Você é um Adulto.")
else:
    print("Você é um Idoso.")