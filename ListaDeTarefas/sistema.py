from arquivoTarefa import *
from interfaceTarefa import *

arq='projetoTarefa.txt'

if not arquivo_existente(arq):
    criar_arquivo(arq)

while True:
    resposta=menu(['Adicionar uma tarefa','Listar tarefas', 'Remover uma tarefa','Sair'])
    if resposta == 1:
        cabeçalho1('ADICIONAR')
        nome_tarefa=input('Digite o nome da tarefa: ')
        descricao_tarefa=input('Digite a descrição da tarefa: ')
        data_tarefa=input('Digite a data em formato dia/mes/ano: ')
        hora_tarefa=input('Digite a hora em formato hora:minuto: ')
        data_hora=data_tarefa+" "+hora_tarefa
        if (validar_data(data_hora)==True):
            armazenar_tarefa(arq, nome_tarefa, descricao_tarefa, data_tarefa, hora_tarefa)
        else:
            print('\033[31mErro, data ou hora inválidas.\033[m')
    elif resposta ==2:
        ler_tarefas(arq)
    elif resposta ==3:
        ler_tarefas(arq)
        num_tarefa=int(input('Digite o numero da tarefa que deseja remover: '))
        remover_tarefa(num_tarefa, arq)
    elif resposta ==4:
        cabeçalho1('Saindo do programa...Até breve!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida.\033[m')
