class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.status = "disponível"

class Membro:
    def __init__(self, nome):
        self.nome = nome
        self.livros_emprestados = []

class Biblioteca:
    def __init__(self):
        self.livros = {}
        self.membros = {}

    def adicionar_livro(self, livro):
        self.livros[livro.titulo] = livro

    def registrar_membro(self, membro):
        self.membros[membro.nome] = membro

    def emprestar_livro(self, titulo_livro, nome_membro):
        livro = self.livros.get(titulo_livro)
        membro = self.membros.get(nome_membro)

        if livro and membro and livro.status == "disponível":
            livro.status = "emprestado"
            membro.livros_emprestados.append(livro)
            print(f"{livro.titulo} emprestado para {membro.nome}")
        else:
            print("Livro não disponível ou membro não encontrado.")

    def retornar_livro(self, titulo_livro, nome_membro):
        livro = self.livros.get(titulo_livro)
        membro = self.membros.get(nome_membro)

        if livro and membro and livro in membro.livros_emprestados:
            livro.status = "disponível"
            membro.livros_emprestados.remove(livro)
            print(f"{livro.titulo} retornado por {membro.nome}")
        else:
            print("Livro não encontrado ou não emprestado para o membro.")

# 
livro1 = Livro("Harry Potter ", "J. K. Rowling")
livro2 = Livro("Diário de um banana", "Jeff Kinney")

membro1 = Membro("João")
membro2 = Membro("Maria")

biblioteca = Biblioteca()
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.registrar_membro(membro1)
biblioteca.registrar_membro(membro2)

biblioteca.emprestar_livro("Harry Potter", "João")

biblioteca.emprestar_livro("Diário de um banana", "Maria")

biblioteca.retornar_livro("Diário de um banana", "Maria")



