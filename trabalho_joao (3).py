from os import system
from time import sleep
import datetime
from funcoes import *
from variaveis import *

##################################################
#    Parte de usar as funções de manipulação de arquivos, usando funções e etc

cardapio = {} #Dicionarios Locais 
login = {}    #Que serão usados aqui
fiscal = {}

salvar_interno = False
dicionarios = (cardapio_dados,banco_login,banco_fiscal) #Dicionarios do arquivo variaveis
locais = [cardapio,login,fiscal]
arquivos = ('cardapio_dados.dat','banco_login.dat','banco_fiscal.dat')

for i,arq in enumerate(arquivos):
    verificar = existe(arq) # Varre no sistema procurando o arquivo
    if verificar: #Arquivo Existe
        print('Arquivo existente!')
        if vazio(arq): #Existe mas está vazio
            if (atualizar(arq,dicionarios[i]) == None):
                print('Erro na escrita do arquivo...')
                salvar_interno = True
            else:
                print('Arquivo escrito com sucesso')


    elif (verificar == False): #Arquivo não existe
        if criar(arq): #Criar Arquivo
            print('Arquivo criado com sucesso!')
            if atualizar(arq,dicionarios[i]): #Transcrever o dicionario ao arquivo
                print('Transcrição de arquivo com sucesso!')

            else: #Erro na transcrição
                print('Erro na transcrição do arquivo')
                salvar_interno = True
        else: #Erro na criação 
            print('Erro na na criação do arquivo')
            salvar_interno = True

    elif (verificar == None): #Erro desconhecido   
        print('Erro na identificação do arquivo')
        salvar_interno = True

    locais[i] = ler(arq) #Leitura do Arquivo para dicionario
    if (locais[i] == None):
        print('Erro na leitura do arquivo')
        salvar_interno = True
    else:
        print('Arquivo lido com sucesso!')
    
    print() 
    print('_-'*30)
    print(f'|| Operação feita para o {1 + i}° Arquivo ||')
    print('_-'*30)
    print()
    sleep(1)

    if (locais[0] != None):
        cardapio = locais[0]
    if (locais[1] != None):
        login = locais[1]
    if (locais[2] != None):
        fiscal = locais[2]

############################################################ 

if salvar_interno:
    print('Manipulação de arquivo externo com erro...modo salvamento interno')

else:
    print('Manipulação de arquivo externo feita com sucesso!')

input("Continuar digite enter".center(100))

##############################################################
#   Código principal em si...

resp = ''
while resp != '9':
    system('cls || clear')
    print(titulo)
    print("\033[1;33m=\033[m"*40)
    print(menu)
    resp = input("Insira a opção que deseja acessar: ")
    
    if resp == '1': #cadastrar
        id_produto = input("Insira o ID do produto para cadastrar: ").strip()  
 
        nome = input(f"Insira o o nome do produto: ")    
        preco = input(f"Insira o preço do {nome}: R$ ")
        preco = verificar_float(preco)
        tempo = input(f"Insira o tempo médio de preparo do {nome}: ")
        
        ingredientes = []
        print("==== DIGITE 0 PARA PARAR ====")
        while True:
            ing = input(f"Insira o {len(ingredientes) + 1}° ingrediente: ").strip()
            if ing == '0':
                break  
            else:
                ingredientes.append(ing)

        cardapio[id_produto] = {
            "nome_exibicao": nome,
                "preco": preco,
            "tempo": tempo,
            "ingredientes": ingredientes,
            "status": True
        }
        if not(salvar_interno):
            if not(atualizar('cardapio_dados.dat',cardapio)):
                print('Erro na transcrição do arquivo')
                salvar_interno = True
                break

        print("\033[1;32mCADASTRO COM SUCESSO! AGUARDANDO O RETORNO\033[m")

        sleep(3)
    
    elif resp == '2': #atualizar
        id_produto = input("Insira o ID do produto para atualizar: ").strip()        
        
        if (id_produto in cardapio) and (cardapio[id_produto]['status']):
            print(f"\033[1;32mPRODUTO ENCONTRADO ({cardapio[id_produto]['nome_exibicao']})!\033[m")
            
            nome = input('Insira o novo nome: ') 
            preco = input("Insira o novo preço: R$ ")
            preco = verificar_float(preco)
            tempo = input("Insira o novo tempo médio de preparo: ")
            
           
            ingredientes = []
            print("==== DIGITE 0 PARA PARAR ====")
            while True:
                ing = input(f"Insira o {len(ingredientes) + 1}° ingrediente: ").strip()
                if ing == '0':
                    break 
                if ing != '0':
                    ingredientes.append(ing)
            
            
            cardapio[id_produto] = {
                "nome_exibicao": nome, 
                "preco": preco,
                "tempo": tempo,
                "ingredientes": ingredientes,
                "status" : True
            }
            
        if not(salvar_interno):
            if not(atualizar('cardapio_dados.dat',cardapio)):
                print('Erro na transcrição do arquivo')
                salvar_interno = True
                break

            print("\033[1;32mATUALIZADO COM SUCESSO! AGUARDANDO O RETORNO\033[m")
        else:
            print("\033[1;31mPRODUTO NÃO ENCONTRADO NO SISTEMA!\033[m")
        sleep(3)
    
    elif resp == '3': #pesquisar
        id_produto = input("Insira o ID do produto para pesquisar: ").strip() 
        
        if (id_produto in cardapio) and (cardapio[id_produto]['status']):
            produto = cardapio[id_produto]

            lista_ingredientes = ", ".join(produto['ingredientes']) #Última linha
            
            print("\033[1;32mPRODUTO ACHADO COM SUCESSO!\033[m")
            print("============================================")
            print(f"NOME            | {produto['nome_exibicao']}")
            print(f"PREÇO           | R${produto['preco']}")
            print(f"TEMPO           | {produto['tempo']}")
            print(f"INGREDIENTES    | {lista_ingredientes}")
            print("============================================")
         
        else:
            
            print("\033[1;31mPRODUTO NÃO ENCONTRADO NO CARDÁPIO!\033[m")
        
        print("\nESPERANDO PARA LEITURA DO USUÁRIO")
        input("Continuar digite enter".center(100))


        
    elif resp == '4': #deletar
        id_produto = input("Insira o ID do produto para deletar: ")
 
        if (id_produto in cardapio) and (cardapio[id_produto]['status']):
            cardapio[id_produto]['status'] = False
            print(f"\033[1;32mPRODUTO '{cardapio[id_produto]['nome_exibicao']}' ENCONTRADO E DELETADO COM SUCESSO!\033[m")
                        
            if not(atualizar('cardapio_dados.dat',cardapio)):
                print('Erro na transcrição do arquivo')
                salvar_interno = True
                break

        else:
            print("\033[1;31mPRODUTO NÃO ENCONTRADO NO SISTEMA!\033[m")
            
        print("AGUARDANDO O RETORNO!")
        sleep(3)

    elif resp == '5': #Cardapio
        print('=' * 50)
        for chave in cardapio:
            if (cardapio[chave]['status']):
                print(f"| {cardapio[chave]['nome_exibicao']:<30} == R${cardapio[chave]['preco']}")
        print('=' * 50)

        input("Continuar digite enter".center(100))

    elif resp == '6': #relatorio
        system('cls || clear')
        
        resp_relatorio = ''
        while resp_relatorio != '5':
            system('cls || clear')
            print(menu_relatorio)
            resp_relatorio = input('Insira a opção que deseja acessar: ')
            if resp_relatorio == '1': #Relatório geral
                mostrar_relatorio(cardapio)
                input("Continuar digite enter".center(100))

            elif resp_relatorio == '2': #Relatório com filtro [preços menores do que 5]
                desejados = []
                for ids in cardapio:
                    if (cardapio[ids]['preco'] <= 5) and (cardapio[ids]['status'] == True):
                        desejados.append(ids)
                if len(desejados) == 0:
                    print()
                    print(' INFELIZMENTE NENHUM PRODUTO SE ENQUADRA NO FILTRO ACIMA... '.center(100,"="))
                else:
                    mostrar_relatorio(cardapio,desejados)
                
                input("Continuar digite enter".center(100))
                
            elif resp_relatorio == '3': #Ordem crescente dos preços 
                                        #funciona também com deletados
                desejados = []
                copia = cardapio.copy()
 
                while len(copia) > 0: #Acha o menor, exclui e procura pelo próximo
                    menor = indice = None
                    for ids,produto in copia.items():
                        if menor == None: #Inicializar a variavel para
                            menor = produto['preco']# fazer a comparação
                            indice = ids

                        if (produto['preco'] < menor):
                            menor = produto['preco']
                            indice = ids
                    desejados.append(indice)
                    del copia[indice]
                
                ordenado_relatorio(cardapio,desejados)                
                input("Continuar digite enter".center(100))
         
            elif resp_relatorio == '4': #campos especificos para selecionar e mostrar...
                print(menu_escolha)
                escolha = input('Insira o campo que deseja filtrar: ')
                print('='*100)

                cabecalho = f"{'NOME':^30}"
                if escolha == '1':
                    cabecalho += f" | {'PREÇO':^7} "
                    filtro = 'preco'
                elif escolha == '2':
                    cabecalho += f" | {'TEMPO':^7} "
                    filtro = 'tempo'
                elif escolha == '3':
                    cabecalho += f" | {'STATUS':^7} "
                    filtro = 'status'
                elif escolha == '4':
                    cabecalho += f" | {'INGREDIENTES':^50} |"
                    filtro = 'ingredientes'
                elif escolha == '5':
                    filtro = None
                else:
                    print('Resposta Inválida')
                    filtro = None

                if (filtro != None):
                    print(cabecalho)
                    for produto in cardapio.values():
                        if (filtro != 'ingredientes'):
                            print(f"{produto['nome_exibicao']:^30} | {str(produto[filtro]):^7}")
                        else:
                            print(f"{produto['nome_exibicao']:^30} | ",end='')
                            for i,ing in enumerate(produto['ingredientes']):
                                if ( (i%7) == 0) and (i != 0):
                                    print()
                                    print(f'{" "*30} | ',end='')
                                else:
                                    print(' '+ing,end='')
                            print()
                
                input("Continuar digite enter".center(100,'='))
         
            elif resp_relatorio != '5':
                print("\033[1;31m Resposta Inválida, tente novamente...\033[m")
               
            else:
                print('Voltando ao menu original')
             
        print("""\033[1m
        FEITO POR: JOÃO VICTOR SILVA MAIA
        PROJETO EM ANDAMENTO AINDA...
        VERSÃO 1.0\033[m
        """)
        
        input("Continuar digite enter".center(100))

    elif resp == '7': #Compras        
        resp_caixa = ''
        while resp_caixa != '3':
            print(menu_caixa) 
            resp_caixa = input('Insira o opção que deseja efetuar: ')

            if resp_caixa == '1': #cadastrar
                nota = gerar_nota_fiscal(fiscal)       
                id_produto = input('Insira o ID do produto que deseja comprar: ')
                cpf = input('Insira o CPF do cliente que deseja efetuar a compra: ')
                if (id_produto in cardapio) and (cpf in login): 
                    print('PRODUTO ENCONTRADO NO CARDÁPIO!')
                    data = str(datetime.date.today()) #2026-07-04 ano, mes, dia
                    data = data[8:] + '/' + data[5:7] + '/' + data[:4]

                    fiscal[nota] = {
                        'id_produto' : id_produto,
                        'preco' : cardapio[id_produto]['preco'],
                        'data' : data, 
                        'cpf' : cpf
                        }
                    if not(salvar_interno):
                        if not(atualizar('banco_fiscal.dat',fiscal)):
                            print('Erro na transcrição do arquivo')
                            salvar_interno = True
                            break

                    print() 
                    print('COMPRA EFETUADA COM SUCESSO! GUARDE O NÚMERO ABAIXO')
                    print(f'SUA NOTA FISCAL É: {nota}')
                    print()
                    input("Continuar digite enter".center(100))

                else:
                    print('Campo inválido, tente novamente...')

 
            elif resp_caixa == '2':#pesquisar
                nota = input('Insira o número da nota fiscal da compra: ')  
                if (nota in fiscal):
                    papel = fiscal[nota]
                    print("\033[1;32mNOTA FISCAL ENCONTRADA COM SUCESSO!\033[m")
                    print("============================================")
                    print(f"ID DO PRODUTO   | {papel['id_produto']}")
                    print(f"PREÇO           | R${papel['preco']}")
                    print(f"DATA            | {papel['data']}")
                    print(f"CPF             | {papel['cpf']}")
                    print("============================================")
                else:
                    print('NOTA FISCAL NÃO ENCONTRADA NA BASE FISCAL')

                print()
                input("Continuar digite enter".center(100))

            elif resp_caixa != '5':
                print("\033[1;31m Resposta Inválida, tente novamente...\033[m")

    elif resp == '8': #Clientes
        resp_clientes = ''
        while resp_clientes != '5':
            system('cls || clear')
            print(menu_clientes)
            resp_clientes = input('Insira a opção que deseja acessar: ')

            if resp_clientes == '1': #cadastrar
                cpf = input('Insira o CPF do cliente: ')                
                if not(cpf in login):
                    nome = input('Insira o nome do cliente: ')
                    telefone = input(f'Insira o telefone de {nome}: ')
                    rua = input(f'Insira a rua de morada de {nome}: ')
                    bairro = input(f'Insira o bairro de morada de {nome}: ')
                    numero_casa = input(f'Insira o número da casa de {nome}: ')
                    login[cpf] = {
                         "nome": nome, 
                         "telefone": telefone,
                         "rua": rua,
                         "bairro": bairro,
                         "numero_casa" : numero_casa,
                         "status" : True
                        }

                    print('CADASTRO REALIZADO COM SUCESSO, AGUARDANDO RETORNO')
                    sleep(3)

                else:
                    print('CPF já cadastrado no banco de login, tente novamente...')
                    sleep(3)

                if not(salvar_interno):
                    if not(atualizar('banco_login.dat',login)):
                        print('Erro na transcrição do arquivo')
                        salvar_interno = True
                        break


 
            elif resp_clientes == '2': #atualizar
                cpf = input("Insira o CPF do cliente para atualizar: ").strip() 
                
                if (cpf in login) and (login[cpf]['status']):
                    pessoa = login[cpf]

                    nome = input('Insira o novo nome do cliente: ')
                    telefone = input(f'Insira o novo telefone de {nome}: ')
                    rua = input(f'Insira a nova rua de morada de {nome}: ')
                    bairro = input(f'Insira o novo bairro de morada de {nome}: ')
                    numero_casa = input(f'Insira o novo número da casa de {nome}: ')
                    login[cpf] = {
                         "nome": nome, 
                         "telefone": telefone,
                         "rua": rua,
                         "bairro": bairro,
                         "numero_casa" : numero_casa,
                         "status" : True
                        }
                else: 
                    print("\033[1;31mPESSOA NÃO ENCONTRADA NO BANCO DE LOGIN!\033[m")

                if not(salvar_interno):
                    if not(atualizar('banco_login',login)):
                        print('Erro na transcrição do arquivo')
                        salvar_interno = True
                        break

                print('PESSOA ATUALIZADA COM SUCESSO! AGUARDANDO O RETORNO')
                sleep(3)

            elif resp_clientes == '3': #pesquisar
                cpf = input("Insira o CPF do cliente para pesquisar: ").strip() 
                
                if (cpf in login) and (login[cpf]['status']):
                    pessoa = login[cpf]

                    print("\033[1;32mPESSOA ENCONTRADA COM SUCESSO!\033[m")
                    print("============================================")
                    print(f"NOME            | {pessoa['nome']}")
                    print(f"TELEFONE        | {pessoa['telefone']}")
                    print(f"RUA             | {pessoa['rua']}")
                    print(f"BAIRRO          | {pessoa['bairro']}")
                    print(f"NÚMERO DA CASA  | {pessoa['numero_casa']}")
                    print("============================================")
                 
                else: 
                    print("\033[1;31mPESSOA NÃO ENCONTRADA NO BANCO DE LOGIN!\033[m")
                
                print("\nESPERANDO PARA LEITURA DO USUÁRIO")
                input("Continuar digite enter".center(100))
            elif resp_clientes == '4': #deletar
                cpf = input("Insira o CPF do cliente para deletar: ")
     
                if (cpf in login) and (login[cpf]['status']):
                    login[cpf]['status'] = False
                    print(f"\033[1;32mPESSOA '{login[cpf]['nome']}' ENCONTRADA E DELETADA COM SUCESSO!\033[m")
                                
                else:
                    print("\033[1;31mPESSOA NÃO ENCONTRADA NO SISTEMA DE LOGIN!\033[m")

                if not(salvar_interno):
                    if not(atualizar('banco_login',login)):
                        print('Erro na transcrição do arquivo')
                        salvar_interno = True
                        break
                        sleep(3)
                print('AGUARDANDO O RETORNO')
                sleep(3)
            elif resp_clientes != '5': #inválido:
                print("\033[1;31m Resposta Inválida, tente novamente...\033[m")
                sleep(3)

    elif resp == '9':
        print("ATÉ LOGO E OBRIGADO!")
    else:
        print("\033[1;31m Resposta Inválida, tente novamente...\033[m")
        sleep(1.5)
