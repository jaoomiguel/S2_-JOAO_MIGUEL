# Sistema simples de cadastro de usuários

usuarios = []  # Lista para armazenar os dicionários de usuários

def cadastrar_usuario():
    nome = input("Digite o nome do usuário: ")
    idade = input("Digite a idade do usuário: ")
    email = input("Digite o email do usuário: ")

    usuario = {
        "nome": nome,
        "idade": idade,
        "email": email
    }

    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")

def consultar_usuario():
    nome_busca = input("Digite o nome do usuário que deseja consultar: ")
    for usuario in usuarios:
        if usuario["nome"] == nome_busca:
            print("Usuário encontrado:")
            print(f"Nome: {usuario['nome']}")
            print(f"Idade: {usuario['idade']}")
            print(f"Email: {usuario['email']}")
            return
    print("Usuário não encontrado.")

def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Cadastrar usuário")
        print("2. Consultar usuário")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            cadastrar_usuario()
        elif escolha == "2":
            consultar_usuario()
        elif escolha == "3":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")




