import os
from dataclasses import dataclass
os.system("cls")

@dataclass
class Paciente:
    nome: str
    idade: int
    peso: float
    altura: float

    def mostrar_dados(self):
        print(f"Nome: {self.nome}\nIdade: {self.idade}\nPeso: {self.peso}\nAltura: {self.altura}")

# Uso da classe
print("======= Solicitando dados do paciente =======")
paciente = Paciente(
    nome=input("Digite seu nome: "),
    idade=int(input("Digite sua idade: ")),
    peso=float(input("Digite seu peso: ")),
    altura=float(input("Digite sua altura: ")) 
)
print(f"---------Exibindo dados do paciente----------")
paciente.mostrar_dados()