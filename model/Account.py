class Account:
    ''' Classe Account: Conta bancária de cada cliente 
        Atributos:
        - username (str) - Nome do usuário (usado no login)
        - password (str) - Senha do usuário (usada no login)
        - balance (int) - Saldo em conta
    '''
    accounts = [] # Lista usada para armazenar as contas quando estas são criadas

    def __init__(self, username, password):
        self.username = username.lower()
        self.password = password.lower()
        self.balance = 0

    # Acrescenta um valor (value) em balance
    def deposit(self, value):
        self.balance += int(value)
        return f'🟢 DEPOSITO EFETUADO: R${str(value)} | SALDO EM CONTA: R${str(self.balance)}'

    # Subtrai um valor (value) de balance, isso, se houver saldo suficiente
    def withdraw(self, value):
        if self.balance >= int(value):
            self.balance -= int(value)
            return f'🔴 SAQUE EFETUADO: R${str(value)} | SALDO EM CONTA: R${str(self.balance)}'
        
        return 'ERROR: Saldo em conta menor que o valor desejado para saque'
