
usuarios = {
    "admin": "admin123",
    "joao": "senha123",
    "maria": "abc456"
}


def validar_login(nome_usuario, senha_digitada):

    if nome_usuario in usuarios:
     
        if usuarios[nome_usuario] == senha_digitada:
            return True 
        else:
            return False 
    else:
        return False 


while True:
    print("\n--- Sistema de Login ---")
    nome_usuario = input("Digite seu nome de usuário (ou 'sair' para fechar): ")
    
  
    if nome_usuario.lower() == 'sair':
        print("👋 Fechando o programa. Até mais!")
        break
    
    senha_digitada = input("Digite sua senha: ")

    
    if validar_login(nome_usuario, senha_digitada):
        print(f"\n🎉 Login bem-sucedido! Bem-vindo(a), {nome_usuario}!")
        break # O login deu certo, então saímos do loop.
    else:
        print("\n❌ Login inválido. Tente novamente.")

