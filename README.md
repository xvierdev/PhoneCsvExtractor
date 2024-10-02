# Extrator de telefones oriundos de arquivos CSV

Esse projeto tem o objetivo de estrair números de telefone oriundos de arquivos .csv provenientes de fontes diversas, pensado para agilizar a o trabalho dos professores ao obterem os telefones dos alunos por meio de formulários online para posteriormente enviar-lhes mensagens e adicionálos aos devidos grupos de turmas no WhatsApp.

# Funções implementadas:

1. Abrir um arquivo csv especificado pelo usuário
1. Localizar a coluna relacionada ao telefone ou perguntar ao usuário caso não seja possível determinar
1. Extrair os telefones da coluna indicada e padronizálos (DDI+DDD+9XXXX-XXXX)
1. Solicitar o nodo do arquivo a ser salvo.
1. Salvar o arquivo com os links redirecionáveis para o whatsapp web para a comunicação com cada telefone.

# Objetivos futuros.

1. Implementar a fucionalidade de ignorar números duplicados.
1. Relatório de erros epecificando as linhas onde o erro ocorre no arquivo csv.
1. Empacotar a aplicação para facilitar a usabilidade.

# Manual de uso

1. Ao executar o script, informe o nome do arquivo csv a ser aberto.
1. Se o script perguntar pela coluna telefone, informe manualmente.
1. Ao final da validação informe o nome do relatório a ser salve. Ex. turma1
1. O arquivo será aberto automaticamente no browser padrão.
