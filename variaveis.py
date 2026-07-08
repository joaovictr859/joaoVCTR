############# DICIONÁRIO PADRÃO PARA TESTAR AS FUNCIONALIDADES #############
#6226
cardapio_dados = {
    "12345": {
        "nome_exibicao": "Hamburguer de Siri",
        "preco": 9.99,
        "tempo": "5 min",
        "ingredientes": ["Pão", "Siri", "Ketchup", "Mostarda", "Alface", "Pickles", "Tomate", "Cebola", "Amor"],
        "status": True
    },
    "54321": {
        "nome_exibicao": "X-Salada",
        "preco": 15.00,
        "tempo": "8 min",
        "ingredientes": ["Pão", "Carne", "Queijo", "Alface", "Tomate", "Maionese"],
        "status": True
    },
    "67890": {
        "nome_exibicao": "Hambúrguer Colorido",
        "preco": 11.99,
        "tempo": "4 min",
        "ingredientes": ["Pão Rosa", "Siri", "Corante Comestível Neon", "Alface", "Queijo Roxo"],
        "status": True
    },
    "13579": {
        "nome_exibicao": "Suco de Alga",
        "preco": 3.50,
        "tempo": "1 min",
        "ingredientes": ["Suco de Alga Concentrado", "Açúcar Recifal", "Traces de Radiação"],
        "status": True
    },
    "24680": {
        "nome_exibicao": "Hambúrguer de Balde",
        "preco": 0.99,
        "tempo": "20 min",
        "ingredientes": ["Isca de Peixe", "Restos Orgânicos", "Lágrimas do Plankton"],
            "status": False
    }
}

banco_fiscal = {
    "1001": {
        "id_produtos": "12345",              # Hambúrguer de Siri
        "total": 9.99,
        "data": "05/07/2026",
        "cpf": "111.111.111-11"             # Bob Esponja
    },
    "1002": {
        "id_produtos": "13579",              # Suco de Alga
        "total": 3.50,
        "data": "05/07/2026",
        "cpf": "111.111.111-11"             # Bob Esponja comprou um suco também
    },
    "1003": {
        "id_produtos": "54321",              # X-Salada
        "total": 15.00,
        "data": "04/07/2026",
        "cpf": "222.222.222-22"             # Patrick Estrela
    },
    "1004": {
        "id_produtos": "67890",              # Hambúrguer Colorido
        "total": 11.99,
        "data": "04/07/2026",
        "cpf": "666.666.666-66"             # Sandy Bochechas
    },
    "1005": {
        "id_produtos": "12345",              # Hambúrguer de Siri
        "total": 9.99,
        "data": "03/07/2026",
        "cpf": "333.333.333-33"             # Lula Molusco
    }
}
#7427
#7870

banco_login = {
    "111.111.111-11": {
        "nome": "Bob Esponja Calça Quadrada",
        "telefone": "(11) 99999-0001",
        "rua": "Rua da Concha",
        "bairro": "Fenda do Biquíni",
        "numero_casa": "124",
        "status": True
    },
    "222.222.222-22": {
        "nome": "Patrick Estrela",
        "telefone": "(11) 99999-0002",
        "rua": "Rua da Concha",
        "bairro": "Fenda do Biquíni",
        "numero_casa": "120",
        "status": True
    },
    "333.333.333-33": {
        "nome": "Lula Molusco Tentáculos",
        "telefone": "(11) 99999-0003",
        "rua": "Rua da Concha",
        "bairro": "Fenda do Biquíni",
        "numero_casa": "122",
        "status": True
    },
    "444.444.444-44": {
        "nome": "Eugene Siriguejo",
        "telefone": "(11) 99999-0004",
        "rua": "Rua da Âncora",
        "bairro": "Fenda do Biquíni",
        "numero_casa": "3541",
        "status": True
    },
    "555.555.555-55": {
        "nome": "Sheldon J. Plankton",
        "telefone": "(11) 99999-0005",
        "rua": "Rua do Balde de Lixo",
        "bairro": "Fenda do Biquíni",
        "numero_casa": "99",
        "status": False  
    },
    "666.666.666-66": {
        "nome": "Sandy Bochechas",
        "telefone": "(11) 99999-0006",
        "rua": "Cúpula da Árvore",
        "bairro": "Fenda do Biquíni",
        "numero_casa": "1",
        "status": True
    }
}


############# MENUS / CABEÇALHOS ##########################
titulo = """\033[1;33m
████  █   █ ████   ███   ████ ████  █   █
█   █ █   █ █   █ █     █     █   █  █ █ 
████  █   █ ████  █  ██  ███  ████    █    
█   █ █   █ █  █  █   █    █  █       █    
████   ███  █   █  ███  ████  █       █    
\033[m"""

menu = (""" --- MENU RESTAURANTE ---
  [1] CADASTRAR PRODUTO
  [2] ATUALIZAR PRODUTO
  [3] PESQUISAR PRODUTO
  [4] DELETAR   PRODUTO
  [5] CARDÁPIO
  [6] RELATÁRIO
  [7] CAIXA
  [8] LOGIN
  [9] SAIR
""")

menu_relatorio = ("""

    [1] RELATÓRIO GERAL
    [2] RELATÓRIO PREÇOS DE ENTRADA
    [3] RELATÓRIO PREÇOS CRESCENTES
    [4] RELATÓRIO POR CAMPO
    [5] SAIR
""")

menu_escolha = ("""
    [1] PREÇO
    [2] TEMPO
    [3] STATUS
    [4] INGREDIENTES
    [5] SAIR
""")

menu_caixa = ("""
    [1] CAIXA REGISTRADORA
    [2] PESQUISAR NOTA
    [3] SAIR
""")

menu_clientes = ("""
    [1] CADASTRAR
    [2] ATUALIZAR
    [3] PESQUISAR
    [4] DELETAR
    [5] SAIR
""")
