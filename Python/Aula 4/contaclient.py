class Conta:

    def __init__(self, conta, nomecliente, tipo):
        self.nomecliente = nomecliente
        self.conta = conta
        self.saldo = 0
        self.status = False
        self.tipo = tipo

    def depositar(self, valor1):
        if self.status == True:
            print(f"Deposito feito com sucesso.")
            self.saldo = valor1
        else:
            print(f"O depositov não foi concluído, pois sua conta está inativa.")

    def sacar(self, valor2):
        if self.status == False:
            print(f"Não foi possível sacar o dinheiro pois a conta está inativa!")
            self.status = False
        else:
            if self.saldo == 0:
                print(f"Não foi possível sacar o dinheiro pois a conta não tem saldo!")
            else:
                print(f'O dinheiro foi sacado com sucesso')
                self.saldo = self.saldo - valor2

    def verificarSaldo(self):
        if self.status == True:
            print(f'O saldo da conta é {self.saldo}!')
            self.status = True
        else:
            print(f'Não é possível ver o saldo pois a conta está inativa!')
            self.status = False

    def ativar(self):
        if self.status == False:
            print(f'A conta foi ativada!')
            self.status = True
        else:
            print(f'Não foi possível ativar a conta pois a mesma ja está ativada!')
            self.status = True

    def desativar(self):
        if self.status == False:
            print(f'Não foi possível desativar a conta pois a mesma ja está desativada!')
            self.status = False
        else:
            if self.saldo != 0:
                print(f'Não foi possível desativar a conta pois é necessario que a conta esteja zerada!')
            else:
                print(f'A conta foi desativada!')
                self.status = False

p2 = Conta(955280, "Kreber", "DACC")
p2.ativar()
p2.ativar()
p2.desativar()
p2.ativar()
p2.depositar(10)
p2.desativar()
p2.depositar(15)
p2.ativar()
p2.depositar(45)
p2.sacar(45)
p2.verificarSaldo()
p2.sacar(45)
p2.desativar()
p2.desativar()
