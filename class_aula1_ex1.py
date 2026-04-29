import os
from dataclasses import dataclass
os.system("cls")

@dataclass
class Pessoa:
    nome: str
    idade: int

@dataclass
class pet:
    nome: str
    idade: int

# Exemplo de uso da classe
pessoa1 = Pessoa(nome="Marta", idade=30)
pessoa2 = Pessoa(nome="Bob", idade=25)
pet1 = pet(nome="Bolt", idade=5)
pet2 = pet(nome="Clark", idade=7)

print(f"Pessoa 1: {pessoa1.nome}\nIdade: {pessoa1.idade}")
print(f"Pet 1: {pet1.nome}\nIdade: {pet1.idade}")
print(f"Pessoa 2: {pessoa2.nome}\nIdade: {pessoa2.idade}")
print(f"Pet 2: {pet2.nome}\nIdade: {pet2.idade}")