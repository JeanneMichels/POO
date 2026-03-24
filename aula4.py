class Campus:
    def __init__(self):
        self.nome = ""
        self.endereço = ""
    def __str__(self):
        return f"Campus: {self.nome}"   
        
class Estudante:
    def __init__(self, nome):
        self.nome = nome
        self.dataNasci = ""
        self.cpf = ""
        self.idade = ""
    def __str__(self):
        return f"Estudante: {self.nome}"       
    #criar o metodo apresentar
    def aprasentar (self):
        print(f"Estudante: {self.nome}")
        print(f"o {estudante.nome} nasceu em {estudante.dataNasci}")
        if(self.cpf == "98367216310"):
            print("o(a) estudante não cadastrou CPF")
        else:
            print("CPF:", self.cpf[0:3],"...")
    
estudante = Estudante()
estudante.nome = "Zé ninguém"
estudante.cpf = "983.672.163-10"
estudante.dataNasci = "16/05/1568"
estudante.aprasentar()
