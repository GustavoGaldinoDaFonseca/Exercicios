import json
import os

db_clientes = "db_clientes.json"
# clientes = []
def carregar_dados():
    if os.path.exists(db_clientes):
        with open(db_clientes, "r", encoding="utf-8") as arq_json:
            return json.load(arq_json)
    else:
        return[]

clientes = carregar_dados()
print(clientes)

def obter_dados_clientes():
    
    nome_cliente = input("Informe o nome do cliente: ")
    nascimento_cliente = int(input("Informe a data de nascimento do cliente: "))
    email_cliente = input("Informe o email do cliente: ")
    rg_cliente = float(input("Informe o rg do cliente: "))
    cpf_cliente = float(input("Informe o cpf do cliente: "))
    estado_cliente = input("Informe o estado do cliente: ")
    cidade_cliente = input("Informe a cidade do cliente: ")
    telefone_cliente = int(input("Informe o número de telefone do cliente: "))

    cliente = {
        "nome_cliente": nome_cliente,
        "nascimento_cliente": nascimento_cliente,
        "email_cliente": email_cliente,
        "rg_cliente": rg_cliente,
        "cpf_cliente": cpf_cliente,
        "estado_cliente": estado_cliente,
        "cidade_cliente": cidade_cliente,
        "telefone_cliente": telefone_cliente

    }

    return cliente

def cadastrar_cliente(dados_cliente):
    clientes.append(dados_cliente)

    return clientes

def mostrar_dados_clientes(dados_cliente):
    for cliente in dados_cliente:
        print(f"""
              Nome Do Cliente: {cliente["nome_cliente"]})
              Nascimento Do Cliente: {cliente["nascimento_cliente"]}")
              Email Do Cliente: {cliente["email_cliente"]}")
              Rg Do Cliente: {cliente["rg_cliente"]}")
              Cpf Do Cliente: {cliente["cpf_cliente"]}")
              Estado Do Cliente: {cliente["estado_cliente"]}")
              Cidade Do Cliente: {cliente["cidade_cliente"]}")
              Telefone Do Cliente: {cliente["telefone_cliente"]}
""")
        
def iniciar_sistema():
    while True:
        print("")
        print("="*80)
        print("Opção 1 - Mostrar Lista de Clientes")
        print("Opção 2 - Cadastrar Clientes")
        print("Opção 3 - Sair do Sistema")
        print("="*80)

        opcao = input("Escolha uma das opções do menu: ")

        if opcao == "1":
            mostrar_dados_clientes(clientes)
        elif opcao == "2":
            cadastrar_cliente(obter_dados_clientes())
        elif opcao == "3":
            print("Sistema finalizado!")
            break
        else:
            print("Opção Invalida, escolha uma das opções do menu.")
















