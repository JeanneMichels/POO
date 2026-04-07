class Aluno:
    def __init__(self, nome, idade, curso, ra, notas):
        self.nome =  nome
        self.idade = idade
        self.curso = curso
        self.ra = ra
        self.notas = notas
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e faço o curso de {self.curso} e meu RA é {self.ra}")
        if(self.ra == ""):
            print("esse aluno não tem RA")
        else:
            print(f"o RA é: {self.ra}")
    def calcular_media(self):
        soma = 0
        for i in range (0, len(self.notas)):
            samo += self.notas[i]
        media = soma / len(self.notas)
        return media
        
    nome = input("qual seu nome? ")
    idade = int (input("qual sua idade?"))
    curso = input("qual o eu curso? ")
    ra = input("qual seu RA?")
    
    aluno1 = Aluno(nome, idade, curso, ra, notas)
    aluno1.apresentar()

    print(f" a media das notas é {aluno1.calcular_media()} ")

class Turma:
    def __init__(self, nome, ano):
        self.nome = nome 
        self.ano = ano 
        self.estudantes = []
    def apresentar(self):
        print(f"{self.nome} - {self.ano}")



# 📖📓🖋️💭
# pra que serve 
# tantos codigos?
# se a vida 
# não é programada
# e as melhores coisas
# não tem logica.

# 📖📓🖋️💭
# Pra que tanto nó em código,
# se a vida não tem roteiro?
# O que é bom não tem lógica,
# nasce do erro, do improviso,
# e transborda o peito inteiro."



class Livro:
    def __init__(self,titulo):
        self.tutulo = titulo
        self.disponivel = True
    def emprestar(self):
        if(self.disponivel == True):
           self.disponivel = False
           print("o livro foi emprestado ")
        else:
           print("o livro não foi empestado")
    
    def devolver(self):
        self.disponivel = True
        print("livro devolvido com sucesso")

livro = Livro("dom casmurro")
livro.emprestar()
livro.devolver()

class Pedido:
    def __init__(self, produto, quantidade, preco_unitario):
        self.produto = produto
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario
   
