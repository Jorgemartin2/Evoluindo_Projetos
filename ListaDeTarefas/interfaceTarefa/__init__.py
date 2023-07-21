def escolha_usuario(msg):
    while True:
        try:
            escolha=int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO! Digite um numero inteiro válido.\033[m')
        except(KeyboardInterrupt):
            print('\033[31mERRO! O usuário preferiu não informar um número.\033[m')
            return 0
        else:
            return escolha
        

def linha(tamanho=40):
    return '='*tamanho


def linha1(tamanho=40):
    return '-'*tamanho


def cabeçalho(txt):
    print(linha())
    print(txt.center(40))
    print(linha())


def cabeçalho1(txt):
    print(linha1())
    print(txt.center(40))
    print(linha1())


def menu(lista):
    cabeçalho('MENU')
    contador=1
    for item in lista:
        print(f'{contador} - {item}')
        contador+=1
    print(linha())
    opção=escolha_usuario('Digite a sua opção: ')
    return opção
