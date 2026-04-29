import os
from dataclasses import dataclass
os.system("cls")

@dataclass
class Cliente:
    nome: str
    email: str
    telefone: int

# Uso da classe
cliente1 = Cliente(nome="Maria", email="maria@gmail.com", telefone="(71)98437-5308")
print(f"Nome: {cliente1.nome}\nEmail: {cliente1.email}\nTelefone: {cliente1.telefone}")