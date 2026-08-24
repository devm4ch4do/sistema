# Sistema de Cadastro e Login

Sistema simples em Python para cadastro de clientes, login e acesso a um menu de usuário.

## Funcionalidades

- Cadastro de clientes
- Login com email e senha
- Validação de campos obrigatórios
- Verificação de email duplicado
- Persistência dos dados em arquivo JSON
- Menu principal e menu do cliente

## Estrutura do Projeto

```text
sistema/
├── main.py
├── clientes.json
├── README.md
└── .gitignore
```

## Como executar

1. Abra o terminal no diretório do projeto.
2. Execute o comando:

```bash
python main.py
```

## Como funciona

### 1. Cadastro
O usuário informa:
- nome
- email
- senha

Esses dados são salvos no arquivo `clientes.json`.

### 2. Login
O usuário informa:
- email
- senha

Se os dados estiverem corretos, o sistema permite o acesso ao menu do cliente.

### 3. Menu do cliente
Após o login, o usuário pode:
- visualizar suas informações
- sair do sistema

## Arquivo de dados

Os clientes são armazenados no arquivo:

```json
clientes.json
```

Exemplo:

```json
[
  {
    "nome": "João",
    "email": "joao@email.com",
    "senha": "123456"
  }
]
```

## Observações

- O sistema salva os clientes em JSON localmente.
- A senha não é criptografada neste projeto.
- O arquivo `clientes.json` será criado automaticamente se não existir.

## Tecnologias utilizadas

- Python 3
- Biblioteca padrão `json`
- Biblioteca padrão `pathlib`

## Autor

Juan Gabriel A Machado / @devm4ch4do

## Licença

Este projeto é de uso livre para fins educacionais.