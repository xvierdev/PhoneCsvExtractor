# Extrator de telefones oriundos de arquivos CSV

Esse projeto tem o objetivo de estrair números de telefone oriundos de arquivos cvs provenientes de fontes diversas, pensado para agilizar a o trabalho dos professores ao obterem os telefones dos alunos por meio de formulários online para posteriormente enviar-lhes mensagens e adicionálos aos devidos grupos de turmas no WhatsApp.

# Requisitos:

1. Abrir um arquivo csv especificado pelo usuário
2. Localizar a coluna relacionada ao telefone ou perguntar ao usuário caso não seja possível determinar
3. Extrair os telefones da coluna indicada e padronizálos
4. Criar um arquivo html com os links redirecionáveis para o whatsapp web para a comunicação com cada telefone.

# Objetivos futuros.

1. Implementar a opção de escolha do nome do arquivo ao salvar.
2. Implementar a fucionalidade de ignorar números duplicados.
3. Empacotar a aplicação para facilitar a usabilidade.

# Utilização do script.

1. Ao executar o script informe a localização do arquivo csv contendo os dados.
2. O script procura pela coluna 'telefone', caso a mesma não existir pergunta ao usuário.
3. Localizada ou indicada a coluna telefone, o script padroniza todos os números removendo espaços e caracteres não numéricos.
4. Ao término do processo é criado um arquivo log.html contendo os links para acesso dos contatos via WhatsApp Web.
