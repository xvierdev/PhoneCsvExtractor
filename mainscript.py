# script de extração de dados de arquivos csv
import os
import webbrowser

DDI = '55'
DDD = '12'
DDI_VALID = ('12', '11')
WPP_WEB = 'https://api.whatsapp.com/send?phone='
START = '<!DOCTYPE html>\n<html>\n<body>'
END = '\n</body>\n</html>'

tel_list = []
total_lines = 0
total_fones = 0

# Verifica se o arquivo existe
def check_filename ():
    while True:
        filename = input('Caminho do arquivo CSV ou exit para sair: ')
        if filename == 'exit' or filename == '':
            exit()
        if filename[-4:] != '.csv':
            filename = filename + '.csv'
        if os.path.exists(filename):
            return filename
        else:
            print(f'Arquivo "{filename}" não encontrado.')

# Pergunta pelo arquivo a ser aberto e abre-o caso o endereço esteja correto ou lança uma excessão se não for possível abrir o arquivo.
def opencsv ():
    file_name = check_filename()
    with open(file_name, 'r') as filecsv:
        global total_lines
        content_lines = filecsv.read().split('\n')
        total_lines = len(content_lines)
        fone_col = find_fone_col(content_lines[0])
        for line in content_lines[1:]:
            new_line =  line.split(',')
            try:
                fone = clean_caracter(new_line[fone_col])
                if valid_number(fone) != False:
                    global total_fones
                    tel_list.append(fone)
                    total_fones += 1
            except IndexError:
                print('Linha inválida.')

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
    criterio2 = len(fone) == 9 and fone[0] == '9'
    criterio3 = len(fone) == 11 and fone[:2] in DDI_VALID
    criterio4 = len(fone) == 13 and fone[:2] == '55'
    fone_valid = criterio1 and (criterio2 or criterio3 or criterio4) 
    return fone_valid

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
        return ''

# Verifica a existência do arquivo e questiona sua sobrescrita
def save_msg ():
    savefile = input('Salvar como: ') + '.html'
    while True:
        if os.path.exists(savefile):
            if input('O arquivo já existe! Sobrescrever? s/n ') == 'n':
                savefile = input('Nome do arquivo: ') + '.html'
            else:
                return savefile
        else:
            return savefile               

# Grava os resultados em um arquivo HTML
def write_results():
    if len(tel_list) > 0:
        filename = save_msg()
        with open(filename, 'w') as filehtml:
            filehtml.write(START)
            for tel in tel_list:
                filehtml.write(f'<a href="{WPP_WEB + tel}">{tel}</a><input type="checkbox"><br>\n')
            filehtml.write(END)
        print(f'{filename} criado com sucesso!')
        webbrowser.open(f'{filename}')
    else:
        print('Nenhum número de telefone válido encontrado.')

opencsv()
print(f'Encontrado {total_fones} telefones em um total de {total_lines} linhas.')
write_results()
input('Pressione enter para fechar.')