import json
from pathlib import Path

ARQUIVO_CLIENTES = Path(__file__).parent / "clientes.json"


def carregar_clientes():
    try:
        with open(ARQUIVO_CLIENTES, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
            return dados if isinstance(dados, list) else []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Arquivo de clientes corrompido. Iniciando com lista vazia.")
        return []


def salvar_clientes(clientes):
    with open(ARQUIVO_CLIENTES, "w", encoding="utf-8") as arquivo:
        json.dump(clientes, arquivo, ensure_ascii=False, indent=4)


def cadastrar_cliente():
    nome = input("Digite seu nome: ").strip()
    email = input("Digite seu email: ").strip().lower()
    senha = input("Digite sua senha: ").strip()

    if not nome or not email or not senha:
        print("Todos os campos são obrigatórios.")
        return

    clientes = carregar_clientes()

    for cliente in clientes:
        if cliente.get("email", "").lower() == email:
            print("Este email já está cadastrado.")
            return

    cliente = {
        "nome": nome,
        "email": email,
        "senha": senha
    }

    clientes.append(cliente)
    salvar_clientes(clientes)

    print("Cadastro realizado com sucesso!")


def login():
    clientes = carregar_clientes()

    while True:
        email = input("Digite seu email: ").strip().lower()
        senha = input("Digite sua senha: ").strip()

        for cliente in clientes:
            if cliente["email"] == email and cliente["senha"] == senha:
                print("Login bem-sucedido!")
                print(f"Bem-vindo, {cliente['nome']}!")
                print(f"Seu email é: {cliente['email']}")
                return cliente

        print("Email ou senha incorretos.")
        opcao = input("Deseja tentar novamente? (s/n): ").strip().lower()

        if opcao != "s":
            return None


def menu_cliente(cliente):
    while True:
        print("\n=======Menu do Cliente=======")
        print("1. Ver informações")
        print("2. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            print(f"\nNome: {cliente['nome']}")
            print(f"Email: {cliente['email']}")
        elif opcao == "2":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")


def menu_principal():
    while True:
        print("\n=======Menu de Login=======")
        print("1. Login")
        print("2. Cadastrar")
        print("3. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cliente = login()
            if cliente:
                menu_cliente(cliente)

        elif opcao == "2":
            cadastrar_cliente()

        elif opcao == "3":
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu_principal()