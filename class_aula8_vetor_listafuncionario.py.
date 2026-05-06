import os
from dataclasses import dataclass
os.system("cls")

@dataclass
class Funcionário:
    nome: str
    idade: int

    def mostrar_dados(self):
        print(f"Nome do funcíonario: {self.nome} ")
        print(f"Idade do funcíonario: {self.idade} ")

quantidade = int(input("Digite o número de Funcíonarios que deseja cadastrar: "))
lista_funcionarios = []

for i in range(quantidade):
    funcionario = Funcionário(
    nome=input("Digite seu nome: "),
    idade=int(input("Digite sua idade: "))
)
    print("============================")
    lista_funcionarios.append(funcionario)

print("===== EXIBINDO DADOS DOS FUNCIONÁRIOS CADASTRADOS=========\n")
for funcionario in lista_funcionarios:
    funcionario.mostrar_dados()

print("======SALVANDO DADOS========")
with open('lista_funcionarios.csv', 'a', encoding='utf-8') as arquivo:
    for funcionario in lista_funcionarios:
        arquivo.write(f"{funcionario.nome}, {funcionario.idade}\n")
    print(f"Salvo com sucesso!")

print(f"Fim de progama.")
