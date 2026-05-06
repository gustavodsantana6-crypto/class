import os
from dataclasses import dataclass

@dataclass
class Livro:
    nome: str
    autor: str
    categoria: str
    preco: float

    def mostrar_dados(self):
        print(f"Nome: {self.nome}\nAutor: {self.autor}\nCaregoria: {self.categoria}\nPreço: {self.preço}\n")

NOME_DO_ARQUIVO = 'catalogo_livros.csv'

# Função para salvar em arquivo.
def salvar_no_arquivo(livro: Livro):
    with open(NOME_DO_ARQUIVO, 'a', encoding='utf-8') as arquivo:
        arquivo.write(f'{livro.nome},{livro.autor},{livro.categoria},{livro.preco}\n')
    print('Livro salvo com sucesso!')

# Função para ler dados em arquivo.
def ler_arquivo():
    # Tratamento de exceção.
    try:
        print('\n- LISTA DE LIVROS -')
        lista_livros = []
        with open(NOME_DO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                nome, autor, categoria, preco = linha.strip().split(',')
                lista_livros.append(Livro(nome, autor, categoria, preco))

        for livro in lista_livros:
            livro.mostrar_dados()
            print('-'*20)
    except FileNotFoundError:
        print('Arquivo não encontrado...')


while True:
    os.system('cls')
    print('''--- SISTEMA DE CADASTRO ---
    1 - Adicionar livro
    2 - Listar livros
    3 - Sair      
         
          ''')
   
    opcao = int(input('Digite a opção desejada: '))

    match opcao:
        case 1:
            os.system('cls')
            print('- Cadastrar livro -')
            novo_livro = Livro(
                nome= input('Nome: '),
                autor=input('Autor:  '),
                categoria=input('Categoria: '),
                preco=float(input('Preço: '))
            )
            salvar_no_arquivo(novo_livro)
        case 2:
            os.system('cls')
            ler_arquivo()
            input('Pressione Enter para voltar ao menu...')
            os.system('cls')
        case 3:
            print('Saindo do programa...')
            break
        case _:
            print('\nOpção inválida. Tente novamente.\n')