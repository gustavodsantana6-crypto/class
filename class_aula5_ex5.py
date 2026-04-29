import os
from dataclasses import dataclass
os.system("cls")

@dataclass
class Paciente:
    nome: str
    idade: int
    peso: float
    altura: float

# Uso da classe
print("= Solicitando dados do paciente =")
paciente = Paciente(
    nome=input("Digite seu nome: "),
    idade=int(input("Digite sua idade: ")),
    peso=float(input("Digite seu peso: ")),
    altura=float(input("Digite sua altura: ")) 
)
print(f"-Exibindo dados do paciente-")
print(f"Nome: {paciente.nome}\nIdade: {paciente.idade}\nPeso: {paciente.peso}\nAltura: {paciente.altura}")