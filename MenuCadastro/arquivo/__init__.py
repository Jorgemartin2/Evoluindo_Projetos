from interface import cabeçalho, linha1


def arquivo_existe(nome):
    try:
        arquivo=open(nome, 'rt')
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True
    

def criar_arquivo(nome):
    try:
        arquivo=open(nome, 'wt+')
        arquivo.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def ler_arquivo(nome):
    try:
        arquivo=open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo.')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        print(f'{"NOME":<18}{"IDADE":<18}{"SEXO":<18}')
        print(linha1())
        for linha in arquivo:
            dado=linha.split(';')
            dado[2]=dado[2].replace('\n', '')
            print(f'{dado[0]:<18}{dado[1]:<18}{dado[2]:<18}')
    finally:
        arquivo.close()


def cadastrar(arq, nome='<desconhecido>', idade=0, sexo=''):
    try:
        arquivo=open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo.')
    else:
        try:    
            arquivo.write(f'{nome};{idade};{sexo}\n')
        except:
            print('Houve um erro na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            arquivo.close()
