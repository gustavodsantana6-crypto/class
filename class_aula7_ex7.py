import os
from dataclasses import dataclass
os.system("cls")

@dataclass
class Endereço:
    logradouro: str
    numero: int

@dataclass
class Cliente:
    nome: str
    idade: int
    endereço: Endereço

    def mostrar_dados(self):
        print(f"Nome: {self.nome}\nIdade: {self.idade}\nEndereço: {self.endereço.logradouro}, {self.endereço.numero}")

print("======= Solicitando dados do cliente =======")
cliente = Cliente(
    nome=input("Digite seu nome: "),
    idade=int(input("Digite sua idade: ")),
    endereço=Endereço(
        logradouro=input("Digite seu logradouro: "),
        numero=int(input("Digite seu número: "))
    )
)
print(f"---------Exibindo dados do cliente----------")
cliente.mostrar_dados()     