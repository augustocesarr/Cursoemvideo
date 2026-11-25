# Declaração de Classe
class Garfanhoto:
    def __init__(self): # Método Construtor
        # Atributos de Instância
        self.nome = ""
        self.idade = 0

    # Métodos de Instância
    def aniversario(self):
        self.idade = self.idade + 1

    def mensagem(self):
        return f"{self.nome} é Garfanhoto(a) e tem {self.idade} anos de idade."

# Declaração de Objetos
g1 = Garfanhoto()
g1.nome = str(input("Digite seu nome: "))
g1.idade = int(input("Digite sua idade: "))
print(g1.mensagem)

g2 = Garfanhoto()
g2.nome = str(input("Digite seu nome: "))
g2.idade = int(input("Digite sua idade: "))
print(g2.mensagem())

