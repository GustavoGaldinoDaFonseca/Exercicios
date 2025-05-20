def cadastrar_filme (nome, descricao, classificação, categoria1, categoria2, categoria3):
    dados_filmes = []
    filme = {
        "nome":nome,
        "descricao": descricao,
        "classificação": classificação,
        "categoria1": [categoria1, categoria2, categoria3]
    }
    dados_filmes. append(filme)
    return dados_filmes

print(cadastrar_filme("Carros","Filme de Ação sobre Carros", "Livre","ação","Aventura"))
    
























































