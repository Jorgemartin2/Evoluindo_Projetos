class ContaBancaria:
    def __init__(self, nome_titular:str, saldo_inicial:float):
        self.nome_titular=nome_titular
        self.saldo=saldo_inicial
        self.extrato=[]
        self.saque_total=0

    def exibir_saldo(self):
        print(f'Saldo atual: R${self.saldo}')
    
    def depositar(self, valor_deposito):
        self.saldo+=valor_deposito
        self.extrato.append('+R$'+str(valor_deposito))
        print(f'Valor R${valor_deposito} foi depositado!')
        self.exibir_saldo()

    def sacar(self, valor_saque):
        taxa=4
        valor_taxa=valor_saque*(taxa/100)
        if (valor_saque+valor_taxa) > self.saldo:
            print('Saldo insuficiente!')
        else:
            self.saque_total+=valor_saque
            limite=1000
            if (self.saque_total>limite):
                print('Limite atingido!')
            else:
                self.saldo-=(valor_saque+valor_taxa)
                self.extrato.append('-R$'+str(valor_saque+valor_taxa))
                print(f'Valor R${valor_saque} foi sacado!')
                print(f'Taxa: R${valor_taxa}')
                self.exibir_saldo()

    def exibir_extrato(self):
        print('\nEXTRATO:')
        for item in self.extrato:
            print(item)
    
    def transferir(self, valor_transferencia, conta_destino):
        if valor_transferencia>self.saldo:
            print('Saldo insuficiente para transferência.')
        else:
            self.saldo-=valor_transferencia
            conta_destino.depositar(valor_transferencia)
            print(f'Transferência de R${valor_transferencia} realizada com sucesso!')
            self.extrato.append('-R$'+str(valor_transferencia))
