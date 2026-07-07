########### MANIPULAÇÃO DE ARQUIVOS EXTERNOS ############################
import pickle
from random import randint

def existe(arquivo):
    try:
        file = open(arquivo,'rb')
        file.close()
        return True
    except FileNotFoundError:
        return False
    except:
        return None

def criar(arquivo):
    try:
        file = open(arquivo,'wb')
        file.close()
        return True
    except:
        return False

def ler(arquivo):
    try:
        file = open(arquivo,'rb')
        dicionario = pickle.load(file)
        file.close()
        return dicionario
    except:
        return None

def atualizar(arquivo,dicio):
    try:
        file = open(arquivo,'wb')
        pickle.dump(dicio,file)
        file.close()
        return True
    except:
        return False

def vazio(arquivo):
    from os import path
    if (path.getsize(arquivo) == 0):
        return True
    else:
        return False

########### FUNÇÕES INTERNAS DO PROGRAMA ###########################

def verificar_float(dado):
    while True:
        try:
            dado = float(dado)
            return dado
        except:
            dado = input('Resposta Inválida, apenas números inteiros: ')

def gerar_nota_fiscal(dicionario): 
    valor = randint(1000,9999)
    while (valor in dicionario): 
        valor = randint(1000,9999)    
    return valor

def mostrar_relatorio(cardapio_dados,filtro=''):
    """
    Mostra o dicionario, sem ordem predefinida com um filtro ou não
    O filtro seria uma lista com indices especificos a ser passados
    Para listarem no dicionário, sem uma ordem pré-definida em es-
    cifica
    """
    print('='*120)
    print(f"{'NOME':^20} | {'PREÇO':^7} | {'TEMPO':^7} | {'STATUS':^7} | {'INGREDIENTES':^50} |")

    if len(filtro) == 0:
        dicionario = cardapio_dados
    else: # Lista com indices especificos de acordo com um filtro
        dicionario = cardapio_dados.copy() #Cria uma cópia e deleta
        for i in cardapio_dados:           #os indices não presentes
            if not(i in filtro):
                del dicionario[i]

    for produto in dicionario.values(): #Observação o 'status' está em string por conta da formatação
        print(f"{produto['nome_exibicao']:^20} | {produto['preco']:^7} | {produto['tempo']:^7} | {str(produto['status']):^7} |",end='')
        for i,ing in enumerate(produto['ingredientes']):
            if ( (i%7) == 0) and (i != 0): #Quebra de linha caso os ingredientes sejam muitos!
                print()
                print(f'{" "*20} | {" "*7} | {" "*7} | {" "*7} |',end='')
            else:
                print(' '+ing,end=',')
        print()

    print('='*120)



def ordenado_relatorio(cardapio_dados,filtro):
    """
    Mostra o dicionario mediante uma ordem especifica
    dada pelos indices dele armazenados numa lista 
    inserida pela variavel filtro
    """
    print('='*120)
    print(f"{'NOME':^20} | {'PREÇO':^7} | {'TEMPO':^7} | {'STATUS':^7} | {'INGREDIENTES':^50} |")

    for indice in filtro:
        produto = cardapio_dados[indice]
        print(f"{produto['nome_exibicao']:^20} | {produto['preco']:^7} | {produto['tempo']:^7} | {str(produto['status']):^7} |",end='')
        for i,ing in enumerate(produto['ingredientes']):
            if ( (i%7) == 0) and (i != 0):
                print()
                print(f'{" "*20} | {" "*7} | {" "*7} | {" "*7} |',end='')
            else:
                print(' '+ing,end='')
        print()

    print('='*120)

#############################################################################
