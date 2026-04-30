import os
from dataclasses import dataclass
os.system("cls")

@dataclass
class Funcionario:
    nome: str
    email: str
    setor: str

    def exibir_dados(self):
        print(f"Nome: {self.nome}\nEmail: {self.email}\nSetor: {self.setor}")

# Uso da classe
print("========= Solicitando dados do funcionário =========")
funcionario = Funcionario(
    nome=input("Digite seu nome: "),
    email=input("Digite seu email: "),
    setor=input(input("Digite o setor: "))
)

print(f"----------Exibindo resultados--------------")
funcionario.exibir_dados()