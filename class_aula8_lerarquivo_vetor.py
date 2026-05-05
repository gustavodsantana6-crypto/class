import os
from dataclasses import dataclass
os.system("cls")

@dataclass
class Funcionário:
    nome: str

    def mostrar_dados(self):
        print(f"Nome do funcíonario: {self.nome}\n")

lista_funcionarios = []

with open('lista_funcionarios.csv', 'r',encoding='utf-8') as arquivo:
    for linha in arquivo:
        nome = linha.strip().split(',')
        lista_funcionarios.append(Funcionário(
        nome=nome
))
for funcionario in lista_funcionarios:
    funcionario.mostrar_dados()

        

