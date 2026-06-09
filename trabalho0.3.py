from os import system
from time import sleep

# BANCO DE DADOS EM MEMÓRIA (Dicionário para salvar os produtos cadastrados)
cardapio_dados = {
    "hamburguer de siri": {
        "nome_exibicao": "Hamburguer de Siri",
        "preco": "9.99",
        "tempo": "5 minutos",
        "ingredientes": ["Pão", "Siri", "Ketchup", "Mostarda", "Alface", "Pickles", "Tomate", "Cebola", "Amor"]
    },
    "x-salada": {
        "nome_exibicao": "X-Salada",
        "preco": "15.00",
        "tempo": "8 minutos",
        "ingredientes": ["Pão", "Carne", "Queijo", "Alface", "Tomate", "Maionese"]
    }
}

l = []
a = []
for x in range(9):
    l.append(0)
for x in range(5):
    a.append(0)

titulo = """\033[1;33m
████  █   █ ████   ███   ████ ████  █   █
█   █ █   █ █   █ █     █    █   █  █ █   
████  █   █ ████  █  ██  ███  ████    █    
█   █ █   █ █  █  █   █    █ █        █    
████   ███  █   █  ███  ████  █        █    
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
        nome = input("Insira o nome do produto para cadastrar: ").strip()
        
        
        if nome == "":
            print("\033[1;31mO nome do produto não pode ser vazio!\033[m")
            sleep(2)
            continue
            
        preco = input(f"Insira o preço do {nome}: R$ ")
        tempo = input(f"Insira o tempo médio de preparo do {nome}: ")
        
        ingredientes = []
        print("==== DIGITE 0 PARA PARAR ====")
        while True:
            ing = input(f"Insira o {len(ingredientes) + 1}° ingrediente: ").strip()
            if ing == '0':
                break  
            if ing != "":
                ingredientes.append(ing)

        cardapio_dados[nome.lower()] = {
            "nome_exibicao": nome,
            "preco": preco,
            "tempo": tempo,
            "ingredientes": ingredientes
        }
        
        print("\033[1;32mCADASTRO COM SUCESSO! AGUARDANDO O RETORNO\033[m")
        sleep(2)
    
    if resp == '2':
        nome = input("Insira o nome do produto para atualizar: ").strip()
        nome_chave = nome.lower() # Padroniza para buscar sem dar erro de maiúsculas
        
        # O "U" do CRUD: Verifica se o produto existe no banco de dados
        if nome_chave in cardapio_dados:
            print(f"\033[1;32mPRODUTO ENCONTRADO ({cardapio_dados[nome_chave]['nome_exibicao']})!\033[m")
            
            # Pede os novos dados
            preco = input(f"Insira o novo preço: R$ ")
            tempo = input(f"Insira o novo tempo médio de preparo: ")
            
            # Coleta os novos ingredientes de forma correta
            ingredientes = []
            print("==== DIGITE 0 PARA PARAR ====")
            while True:
                ing = input(f"Insira o {len(ingredientes) + 1}° ingrediente: ").strip()
                if ing == '0':
                    break # Para o loop sem colocar o '0' dentro da lista
                if ing != "":
                    ingredientes.append(ing)
            
            # ATUALIZAÇÃO NO DICIONÁRIO: Substitui os dados antigos pelos novos
            cardapio_dados[nome_chave] = {
                "nome_exibicao": cardapio_dados[nome_chave]['nome_exibicao'], # Mantém o nome original bonito
                "preco": preco,
                "tempo": tempo,
                "ingredientes": ingredientes
            }
            
            print("\033[1;32mATUALIZADO COM SUCESSO! AGUARDANDO O RETORNO\033[m")
        else:
            # Se o produto não existir no dicionário:
            print("\033[1;31mPRODUTO NÃO ENCONTRADO NO SISTEMA!\033[m")
            
        sleep(3)
    
    elif resp == '3':
        nome = input("Insira o nome do produto para pesquisar: ").strip()
        nome_chave = nome.lower() # Padroniza para buscar o item mesmo se digitar Maiúsculo/Minúsculo
        
        # O "R" (Read) do CRUD: Verifica se o lanche existe nas chaves do dicionário
        if nome_chave in cardapio_dados:
            produto = cardapio_dados[nome_chave]
            
            # Pega a lista de ingredientes e transforma em um texto bonito separado por vírgulas
            lista_ingredientes = ", ".join(produto['ingredientes'])
            
            print("\033[1;32mPRODUTO ACHADO COM SUCESSO!\033[m")
            print("============================================")
            print(f"NOME            | {produto['nome_exibicao']}")
            print(f"PREÇO           | R${produto['preco']}")
            print(f"TEMPO           | {produto['tempo']}")
            print(f"INGREDIENTES    | {lista_ingredientes}")
            print("============================================")
        else:
            # Caso o usuário digite algo que não está no dicionário
            print("\033[1;31mPRODUTO NÃO ENCONTRADO NO CARDÁPIO!\033[m")
        
        print("\nESPERANDO PARA LEITURA DO USUÁRIO")
        input("Continuar digite enter".center(100))
        
    if resp == '4':
        nome = input("Insira o nome do produto para deletar: ").strip()
        nome_chave = nome.lower() # Padroniza a string para evitar erros de maiúsculas/minúsculas
        
        # O "D" (Delete) do CRUD: Verifica se o lanche existe nas chaves do dicionário
        if nome_chave in cardapio_dados:
            
            # Executa a remoção real do item do "banco de dados"
            del cardapio_dados[nome_chave]
            
            print(f"\033[1;32mPRODUTO '{nome}' ENCONTRADO E DELETADO COM SUCESSO!\033[m")
        else:
            # Se o usuário digitar um nome que não existe no dicionário:
            print("\033[1;31mPRODUTO NÃO ENCONTRADO NO SISTEMA!\033[m")
            
        print("AGUARDANDO O RETORNO!")
        sleep(3)

    elif resp == '5': #cardapio
        print("""
        ===========================
        BAURU       R$6
        X-SALADA    R$7
        X-BURGUER   R$10
        X-TUDO      R$18
        OLHO GRANDE R$30
        IMORTAL     R$40
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