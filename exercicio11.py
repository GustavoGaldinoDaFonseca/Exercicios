import json
import os

db_veiculos = "db_veiculos.json"

def carregar_dados():
    if os.path.exists(db_veiculos):
        with open(db_veiculos, "r", encoding="utf-8") as arq_json:
            return json.load(arq_json)
    else:
        return []

def obter_dados_veiculo():
    marca_veiculo = input("INFORME A MARCA DO VEÍCULO: ")
    modelo_veiculo = input("INFORME O MODELO DO VEÍCULO: ")
    ano_veiculo = input("INFORME O ANO DO VEÍCULO: ")
    cor_veiculo = input("INFORME A COR DO VEÍCULO: ")

    veiculo = {
        "marca": marca_veiculo,
        "modelo": modelo_veiculo,
        "ano": ano_veiculo,
        "cor": cor_veiculo
    }

    return veiculo

def cadastrar_veiculo(dados_veiculo):
    veiculos = carregar_dados()
    veiculos.append(dados_veiculo)

    with open(db_veiculos, "w", encoding="utf-8") as arq_json:
        json.dump(veiculos, arq_json, indent=4, ensure_ascii=False)

def mostrar_dados_veiculos(veiculos):
    if not veiculos:
        print("Nenhum veículo cadastrado no momento.")
    else:
        for veiculo in veiculos:
            print(f"""
            Marca do Veículo: {veiculo["marca"]}
            Modelo do Veículo: {veiculo["modelo"]}
            Ano de Fabricação do Veículo: {veiculo["ano"]}
            Cor do Veículo: {veiculo["cor"]}
            """)

def iniciar_sistema():
    veiculos = carregar_dados()
    while True:
        print("")
        print("=" * 80)
        print("Opção 1 - Mostrar Lista de Veículos")
        print("Opção 2 - Cadastrar Veículo")
        print("Opção 3 - Sair do Sistema")
        print("=" * 80)

        opcao = input("Escolha uma das opções do Menu: ")

        if opcao == "1":
            mostrar_dados_veiculos(veiculos)
        elif opcao == "2":
            cadastrar_veiculo(obter_dados_veiculo())
            veiculos = carregar_dados()
        elif opcao == "3":
            print("Sistema Finalizado")
            break
        else:
            print("Opção inválida, escolha uma das opções no menu.")

if __name__ == "__main__":
    iniciar_sistema()
