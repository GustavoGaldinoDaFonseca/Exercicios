import json
import os

data = "veiculo_json"

def carregar_dados ()
    if os.path.exists(data):
        with open(data,"r",encoding="utf-8") as arq_json:
            return json.load(arq_json)
    else:
        return[]
    
def obter_dados():
modelo_do_carro = input("informar o modelo do veiculo:")
marca_do_veiculo = input ("informar a marca do veiculo:")
ano_de_fabricação = input ("ano de fabricação:")
cor_do_carro = input ("cor do veiculo:")

veiculo =(
    "modelo_do_carro": modelo_do_carro
    "marca_do_carro":  marca_do_carro
    "ano_de_fabrcação": ano_de_fabricação
    "cor_do_carro": cor_do_carro

)
def cadastrar_veiculos(receber veiculos)
db_veiculos = carregar_dados
db_veiculos.append




































































































































