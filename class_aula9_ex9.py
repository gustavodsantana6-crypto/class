import os
from dataclasses import dataclass
os.system("cls")

@dataclass
class Empresa:
    nome: str
    cnpj: str
    telefone: str

    def mostrar_dados(self):
        print(f"Nome da empresa: {self.nome}\nCnpj da empresa: {self.cnpj}\nTelefone da empresa: {self.telefone}")

quantidade = int(input("Digite a quantidade de empresas que voçê deseja adicionar: "))
lista_empresas = []        

# Uso da classe.
for i in range(quantidade):
    print("===========================")
    empresa = Empresa(
        nome=input("Digite o nome da empresa: "),
        cnpj=input("Digite o cnpj da empresa: "),
        telefone=input("Digite o telefone da empresa: ")
    )
    lista_empresas.append(empresa)

print(f"---------Exibindo dados das empresas cadastradas---------")
for empresa in lista_empresas:
      empresa.mostrar_dados()

print(f"======SALVANDO DADOS=======")
with open("contato_empresas.csv","a", encoding="utf-8") as arquivo:
    for empresa in lista_empresas:
           arquivo.write(f"{empresa.nome},{empresa.cnpj},{empresa.telefone}\n")
    print(f"Salvo com sucesso!")

print(f"Fim do progama.")



