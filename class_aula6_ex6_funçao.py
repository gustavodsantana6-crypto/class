import os
from dataclasses import dataclass
os.system("cls")

@dataclass
class Fornecedor:
    nome: str
    email: str
    telefone: int
    endereço: str

    def mostrar_dados(self):
        print(f"Nome: {self.nome}\nEmail: {self.email}\nTelefone: {self.telefone}\nEndereço: {self.endereço}")

# Uso da classe
print("======= Solicitando dados do fornecedor =======")
fornecedor = Fornecedor(
    nome=input("Digite o nome do fornecedor: "),
    email=input("Digite o email do fornecedor: "),
    telefone=int(input("Digite o telefone do fornecedor: ")),
    endereço=input("Digite o endereço do fornecedor: ")
)
print(f"------Exibindo dados do fornecedor-------")
fornecedor.mostrar_dados()