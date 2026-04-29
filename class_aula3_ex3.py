import os
from dataclasses import dataclass
os.system("cls")

@dataclass
class Funcionário:
    nome: str
    matricula: int
    email: str
    setor: str

# Uso da classe
funcionario1 = Funcionário(nome="Gustavo", matricula="14253647", email="gustavoporo823@gmail.com", setor="TI")
print(f"Nome: {funcionario1.nome}\nMatrícula: {funcionario1.matricula}\nEmail: {funcionario1.email}\nSetor: {funcionario1.setor}")