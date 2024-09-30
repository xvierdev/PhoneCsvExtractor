# script de extração de dados de arquivos csv
import os
import webbrowser

DDI = '55'
DDD = '12'
tel_list = []
total_lines = 0
total_fones = 0
WPP_WEB = 'https://api.whatsapp.com/send?phone='

# Pergunta pelo arquivo a ser aberto e abre-o caso o endereço esteja correto ou lança uma exessão se não for possível abrir o arquivo.
def opencsv ():
    global filename, total_fones, total_lines
    filename = input('Digite o caminho do arquivo ou exit para sair:')
    if filename == 'exit':
        exit()
    while True:
        try:
            with open(filename, 'r') as filecsv:
                content_lines = filecsv.read().split('\n')
                fone_col = find_fone_col(content_lines[0])
                for line in content_lines[1:]:
                    total_lines += 1
                    fone = clean_caracter(line.split(',')[fone_col])
                    if fone != False:
                        tel_list.append(fone)
                        total_fones += 1
                break
        except FileNotFoundError:
            print('Arquivo não encontrado!')


# Encontra a coluna com o termo 'telefone'
def find_fone_col(data):
    cols = data.split(',')
    cont = 0
    for cell in cols:
        if 'Telefone' in cell or 'telefone' in cell or 'fone' in cell:
            return cont
        else:
            cont += 1
    return False

# Valida o número de telefone.
def valid_number(fone):
    criterio1 = fone.isnumeric()
    criterio2 = len(fone) >= 9
    criterio3 = len(fone) <= 11
    criterio4 = len(fone) == 13 and fone[:2] == '55'
    return criterio1 and (criterio1 and criterio3 or criterio4)

# limpa os caracter indesejáveis do número de telefone e acrescenta o DDI e DDD se necessário.
def clean_caracter (fone):
    fone = fone.replace('"', '').replace('(', '').replace(')', '').replace(' ', '').replace('-', '').replace('+', '')
    if valid_number(fone):
        if len(fone) == 9:
            fone = DDI + DDD + fone
        elif len(fone) == 11:
            fone = DDI + fone
        return fone
    else:
        return False

# Grava os resultados em um arquivo HTML
def write_results():
    savefile = 'log.html'
    start = '<!DOCTYPE html>\n<html>\n<body>'
    end = '\n</body>\n</html>'
    with open(savefile, 'w') as filehtml:
        filehtml.write(start)
        for tel in tel_list:
            filehtml.write(f'<a href="{WPP_WEB + tel}">{tel}</a><input type="checkbox"><br>\n')
        filehtml.write(end)
    print('log.html criado com sucesso.')
    webbrowser.open('log.html')

opencsv()
print(f'Encontrado {total_fones} telefones em um total de {total_lines} linhas.')
write_results()
input('Pressione enter para fechar.')