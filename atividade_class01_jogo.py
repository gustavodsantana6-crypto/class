´´´´´´´´´´´´´´´´´´´´´´´´´´´´import os
from dataclasses import dataclass

def limpar_tela():
    # Funciona no Windows ('nt') e no Linux/Mac ('posix')
    os.system('cls' if os.name == 'nt' else 'clear')

limpar_tela()

@dataclass
class Jogo:
    nome: str
    criador: str
    categoria: str
    preco: float

    def mostrar_dados(self):
        print(f"Nome do game: {self.nome}\nCriador: {self.criador}\nCategoria: {self.categoria}\nPreço: R$ {self.preco:.2f}\n")

NOME_DO_ARQUIVO = "catalogo_jogos.csv"

def salvar_no_arquivo(jogo: Jogo):
    with open(NOME_DO_ARQUIVO, 'a', encoding='utf-8') as arquivo:
        # Salva separado apenas por vírgula, sem espaços, para facilitar a leitura
        arquivo.write(f"{jogo.nome},{jogo.criador},{jogo.categoria},{jogo.preco}\n")
        print("Jogo salvo com sucesso!\n")

def ler_arquivo():
    try:
        print("\n- LISTA DE GAMES -")
        lista_jogos = []
        
        with open(NOME_DO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                # O split separa a linha em 4 variáveis
                nome, criador, categoria, preco = linha.strip().split(',')
                lista_jogos.append(Jogo(nome, criador, categoria, float(preco)))

        # O loop de impressão deve ficar FORA do loop de leitura
        for jogo in lista_jogos:
            jogo.mostrar_dados()
            print('-'*20)
            
    except FileNotFoundError:
        print("Arquivo não encontrado. Adicione um jogo primeiro!")
    except ValueError:
        print("Erro ao ler os dados. O formato do arquivo pode estar corrompido.")

while True:
    print("""--- SISTEMA DE GAMES ---
        1 - Adicionar game
        2 - Analisar games na sua caixa
        3 - Sair
    """)
    
    try:
        opcao = int(input("Escolha uma das opções acima: "))
    except ValueError:
        print("\nOpção inválida! Por favor, digite um número.\n")
        continue

    match opcao:
        case 1:
            limpar_tela()
            print("- Adicionar game -")
            try:
                # Removidas as aspas triplas para os inputs funcionarem de verdade
                novo_jogo = Jogo(
                    nome=input('Nome: '),
                    criador=input('Criador: '),
                    categoria=input('Categoria: '),
                    preco=float(input('Preço: '))
                )
                salvar_no_arquivo(novo_jogo)
            except ValueError:
                print("Erro: O preço deve ser um número válido!")
                
        case 2:
            limpar_tela()
            print("- Analisar jogos -")
            ler_arquivo()
            input("Pressione Enter para voltar ao menu...")
            limpar_tela()
            
        case 3:
            limpar_tela()
            print("Saindo do programa...")
            break
            
        case _:
            print("\nOpção inválida. Tente novamente!\n")
