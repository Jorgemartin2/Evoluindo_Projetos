def LeiaInt(msg):
    while True:
        try:
            n=int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite um numero inteiro válido!\033[m')
        except (KeyboardInterrupt):
            print('\033[31mERRO: O usuário preferiu não informar o número.\033[31m')
            return 0
        else:
            return n


def linha(tam=42):
    return '='*tam


def linha1(tam=42):
    return '-'*tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    contador=1
    for item in lista:
        print(f'{contador} - {item}')
        contador+=1
    print(linha1())
    opção=LeiaInt('Sua opção: ')
    return opção
