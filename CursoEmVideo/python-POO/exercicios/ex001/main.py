# Declaração de Classe
class Garfanhoto:
    def __init__(self): # Método Construtor
        # Atributos de Instância
        self.nome = ""
        self.idade = 0

    # Métodos de Instância
    def aniversario(self):
        self.idade = self.idade + 1

    def __str__(self):
        return f"{self.nome} é Garfanhoto(a) e tem {self.idade} anos de idade."

# Declaração de Objetos
g1 = Garfanhoto()
g1.nome = "Augusto"
g1.idade = 18
print(g1)
