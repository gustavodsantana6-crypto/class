import os
from dataclasses import dataclass
os.system("cls")

@dataclass
class Cliente:
    nome: str
    email: str
    telefone: int

# Uso da classe
print("= Solicitando dados do cliente =")
cliente = Cliente(
    nome=input("Digite seu nome: "),
    email=input("Digite seu email: "),
    telefone=int(input("Digite seu telefone: "))
)

print(f"-Exibindo dados do cliente-")
print(f"Nome: {cliente.nome}\nEmail: {cliente.email}\nTelefone: {cliente.telefone}")