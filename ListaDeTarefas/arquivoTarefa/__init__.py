from interfaceTarefa import *
from datetime import datetime

def criar_arquivo(nome):
    try:
        arquivo=open (nome, 'wt+')
        arquivo.close()
    except:
        print('\033[31mHouve um erro na criação do arquivo.\033[m')
    else:
        print(f'\033[33mArquivo {nome} criado com sucesso.\033[m')


def arquivo_existente(nome):
    try:
        arquivo=open (nome, 'rt')
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True


def armazenar_tarefa(arq, nome='<tarefa desconhecida>', descricao='<sem descrição>', data=0, hora=0):
    try:
        with open(arq, 'at') as arquivo:
            arquivo.write(f'{nome};{descricao};{data};{hora}\n')
    except:
        print('\033[31mHouve um erro ao adicionar os dados.\033[m')
    else:
        print(f'\033[32mNova tarefa {nome} adicionada.\033[m')


def ler_tarefas(nome):
    try:
        with open(nome, 'rt') as arquivo:
            tarefas=arquivo.readlines()
    except:
        print('\033[31mErro ao ler o arquivo.\033[m')
    else:
        cabeçalho('LISTAGEM DAS TAREFAS')
        for indice, item in enumerate(tarefas):
            print(f'TAREFA NUMERO {indice+1}')
            print(linha1())
            dados=item.split(';')
            print(f'Nome: {dados[0]}')
            print(f'Descrição: {dados[1]}')
            print(f'Data: {dados[2]}')
            print(f'Hora: {dados[3]}')
            print()


def remover_tarefa(indice, arq):
    try:
        with open(arq, 'r') as arquivo:
            tarefas=arquivo.readlines()
    except:
        print('\033[31mHouve um erro ao abrir o arquivo.\033[m')
    try:
        ponteiro=0
        with open(arq, 'w') as lista:
            for tarefa in tarefas:
                if ponteiro != (indice-1):
                    lista.write(tarefa)
                ponteiro+=1
        print(f'\033[32mTarefa {indice} removida com sucesso.\033[m')
    except:
        print(f'\033[31mTarefa {indice} não existe.\033[m')            


def validar_data(data_hora):
    try:
        datetime.strptime(data_hora, '%d/%m/%Y %H:%M')
        return True
    except:
        return False
