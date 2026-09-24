def calculadora_divisao(numerador, denominador):
    """
    Função para realizar a divisão de dois números com tratamento de erros.
    
    Parâmetros:
    - numerador (float/int): O número que será dividido.
    - denominador (float/int): O número pelo qual vamos dividir.
    """
    try:
        
        resultado = numerador / denominador
        return f"Resultado da divisão: {resultado}"
        
    except ZeroDivisionError:
      
        return "Erro: Não é possível realizar divisão por zero!"




print("--- Teste 1 ---")
print(calculadora_divisao(10, 2))

print("\n--- Teste 2 ---")
print(calculadora_divisao(10, 0))