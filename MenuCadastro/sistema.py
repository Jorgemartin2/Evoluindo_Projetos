from interface import *
from time import sleep
from arquivo import *

arq='projetoiniciante.txt'

if not arquivo_existe(arq):
    criar_arquivo(arq)

while True:
    resposta=menu(['Ver pessoas cadastradas','Cadastrar nova pessoa','Sair do sistema'])
    if resposta == 1:
        ler_arquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome=str(input('Nome: '))
        idade=LeiaInt('Idade: ')
        sexo=str(input('Sexo: '))
        cadastrar(arq, nome, idade, sexo)
    elif resposta == 3:
        cabeçalho('Saindo do sistema...Até mais!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida.\033[m')
    sleep(2)
