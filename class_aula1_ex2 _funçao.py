import os
from dataclasses import dataclass
os.system("cls")

@dataclass
class Cliente:
    nome: str
    email: str
    telefone: int

    def mostrar_dados(self):
        print(f"Nome: {self.nome}\nEmail: {self.email}\nTelefone: {self.telefone}")

# Uso da classe
print("======= Solicitando dados do cliente =======")
cliente = Cliente(
    nome=input("Digite seu nome: "),
    email=input("Digite seu email: "),
    telefone=int(input("Digite seu telefone: "))
)
print(f"------Exibindo dados do cliente-------")
cliente.mostrar_dados()