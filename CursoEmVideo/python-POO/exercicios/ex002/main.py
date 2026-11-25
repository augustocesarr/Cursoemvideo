# Declaração de Classe
class Garfanhoto:
    """
Essa classe cria um Garfanhoto, que é uma pessoa que tem nome e idade.

Para criar uma nova pessoa, use:
variavel = Garfanhoto(nome, idade)
    """
    def __init__(self, nome = "nulo", idade = 0): # Método Construtor
        # Atributos de Instância
        self.nome = nome
        self.idade = idade

    # Métodos de Instância
    def aniversario(self):
        self.idade = self.idade + 1

    def __str__(self): # Dunder Method
        return f"{self.nome} é Garfanhoto(a) e tem {self.idade} anos de idade."

    def __getstate__(self):
        return f"Estado: nome = {self.nome} ; idade = {self.idade}"

# Declaração de Objetos
g1 = Garfanhoto("Maria", 17)
g1.aniversario()
print(g1)

print(g1.__dict__) # Attribute
print(g1.__getstate__()) # Method - Ele pode ser personalizado, programando um Estado para ser mostrado
print(g1.__class__) # Dunder Attribute 
print(g1.__doc__) # Dunder Attribute 