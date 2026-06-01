from os import system
from time import sleep
l = []
a = []
for x in range(9):
    l.append(0)
for x in range(5):
    a.append(0)


titulo = """\033[1;33m
████  █   █ ████   ███   ████ ████  █   █
█   █ █   █ █   █ █     █     █   █  █ █   
████  █   █ ████  █  ██  ███  ████    █    
█   █ █   █ █  █  █   █     █ █       █    
████   ███  █   █  ███  ████  █       █    
\033[m"""

menu = ("""
    [1] CADASTRAR
    [2] ATUALIZAR
    [3] PESQUISAR
    [4] DELETAR
    [5] CARDÁPIO
    [6] RELATÁRIO
    [7] SAIR
    """)

resp = 0
while resp != '7':
    system('cls || clear')
    print(titulo)
    print("\033[1;33m=\033[m"*40)
    print(menu)
    resp = input("Insira a opção que deseja acessar: ")
    
    
    if resp == '1':
        nome = input("Insira o nome do produto para cadastrar: ")
        preco = input(f"Insira o preço do {nome}: ")
        tempo = input(f"Insira o tempo médio de preparo do {nome}: ")
        ingredientes = []
        ing = ""
        print("==== DIGITE 0 PARA PARAR ====")
        while (ing != '0'):
            ing = input(f"Insira o {len(ingredientes) + 1}° ingrediente: ")
            ingredientes.append(ing)
        ingredientes[-1] = ""
        print("CADASTRO COM SUCESSO! AGUARDANDO O RETORNO")
        sleep(3)
    elif resp == '2':
        nome = input("Insira o nome do produto para atualizar: ")
        print("PRODUTO ENCONTRADO!")
        preco = input(f"Insira o novo preço do {nome}: ")
        tempo = input(f"Insira o novo tempo médio de preparo do: {nome}")
        ingredientes = []
        ing = ""
        print("==== DIGITE 0 PARA PARAR ====")
        while (ing != '0'):
            ing = input(f"Insira o {len(ingredientes) + 1}° ingrediente: ")
            ingredientes.append(ing)
        print("ATUALIZADO COM SUCESSO! AGUARDANDO O RETORNO")
        sleep(3)
    elif resp == '3':
        nome = input("Insira o nome do produto para pesquisar: ")
        print("PRODUTO ACHADO COM SUCESSO!")
        
        print("""============================================
        NOME            | HAMBURGUER DE SIRI
        PREÇO           | R$9.99
        TEMPO           | 5 minutos
        INGREDIENTES    | Pão,siri, ketchup, mostarda, alface, pickles, tomate, cebola e amor 
        ============================================""")
        
        print("ESPERANDO PARA LEITURA DO USUÁRIO")
        input("Continuar digite enter".center(100))
    elif resp == '4':
        nome = input("Insira o nome do produto para deletar: ")
        print("PRODUTO ENCONTRADO E DELETADO COM SUCESSO!")
        print("AGUARDANDO O RETORNO!")
        sleep(3)
        
    elif resp == '5': #cardapio
        print("""
        ===========================
        X-BURGUER R$9,99
        X-BURGUER R$9,99
        X-BURGUER R$9,99
        X-BURGUER R$9,99
        ===========================
        """)
        input("Continuar digite enter".center(100))
    elif resp == '6': 
        print("""\033[1m
        FEITO POR: JOÃO VICTOR SILVA MAIA
        PROJETO EM ANDAMENTO AINDA...
        VERSÃO 1.0\033[m
        """)
        input("Continuar digite enter".center(100))
    
    elif resp == '7':
        print("ATÉ LOGO E OBRIGADO!")
    else:
        print("\033[1;31m Resposta Inválida, tente novamente...")
        sleep(1.5)