from exercicios4 import calcular_media

alunos = []

def obter_dados_alunos():
    nome_aluno = input("Informe seu nome completo")
    email_aluno = input("Informe o email do aluno")
    serie_aluno = input("Informe a serie do aluno")
    nota01 = float(input("Informe a primeira nota do aluno"))
    nota02 = float(input("Informe a segunda nota do aluno"))
    nota03 = float(input("Informe a terceira nota do aluno"))

    return cadastrar_aluno(nome_aluno, email_aluno, serie_aluno, nota01, nota02, nota03)

def cadastrar_aluno(nome, email, serie, nota01= 0, nota02= 0, nota03= 0,):
     

    notas = [nota01, nota02, nota03]

    aluno = {
            "nome": nome,
            "email": email,
            "serie": serie,
            "notas": notas,
            "media": calcular_media(notas)
}
    alunos.append(aluno)

    return alunos


def mostrar_dados_alunos(dados_alunos):
    for aluno in dados_alunos:
        print(f"Nome do aluno: {aluno["nome"]} | Email do aluno: {aluno["email"]} | Série do aluno {aluno["serie"]} | Notas do aluno{aluno["notas"]} Média do aluno {aluno["media"]}")

    return
def iniciar_sistema():
    while True:
        print("="*80)
        print("Opção 1 => Mostrar lista de Alunos Cadastrados")
        print("Opção 2 => Cadastrar Alunos")
        print("Opção 3 => Sair Do Sistema")
        print("="*80)

        opcao = input("Escolha uma das opções acima")

        if opcao == "1":
            mostrar_dados_alunos()
        elif opcao == "2":
            obter_dados_alunos()
        else:
            print("Sistema finalizado")
            break

iniciar_sistema()































