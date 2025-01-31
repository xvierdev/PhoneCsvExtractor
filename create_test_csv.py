# Criador de arquivos csv de teste de extração dos telefones
from random import randint

try:
    filename = input('Nome do arquivo a ser criado: ')
    qtd_lines = int(input('Quantidade de Registros: '))
    with open(f'{filename}.csv', 'w') as test_csv:
        test_csv.write(f'"username", "telefone", "email"\n')    # cabeçalho do arquivo csv
        for i in range(qtd_lines):
            test_csv.write(f'"username", "{randint(100000000, 99999999999)}", "user@email.com"\n')
except ValueError:
    print('O valor informádo é do tipo inválido.')
