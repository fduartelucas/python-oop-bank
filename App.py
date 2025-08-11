from model.Account import Account

def wrong_option(prefix=''):
    print(f'{prefix}ERROR: Digite uma opção válida')

def use_account(username, selected_account):
    ''' Função: Gerencia a conta e saldo de cada usuário (Depósitos e saques)
        Parâmetros:
        - username (str) - Nome do usuário, será utilizado em alguns prints compondo o menu
        - selected_account (Object) - Objeto da classe Account (Conta específica a ser gerenciada)
    ''' 
    
    # Laço que se repete até que seja selecionada a opção "k" para sair da conta.
    while True:
        user_input = input(f'\nInício > {username} > Digite "d" para DEPOSITAR, "s" para SACAR ou "k" para SAIR DA CONTA\nInício > {username} > ')

        # "d" para DEPOSITAR
        if user_input.lower() == 'd':
            user_input = input(f'\nInício > {username} > Digite o VALOR A SER DEPOSITADO: ')
            print(f'Início > {username} > {selected_account.deposit(user_input)}')
        # "s" para SACAR
        elif user_input.lower() == 's':
            user_input = input(f'\nInício > {username} > Digite o VALOR A SER SACADO: ')
            print(f'Início > {username} > {selected_account.withdraw(user_input)}')
        # "k" para SAIR DA CONTA
        elif user_input.lower() == 'k':
            break
        # Imprime erro, cajo nenhuma opção válida seja digitada ou seja digitado algo por acidente.
        else:
            wrong_option(f'Início > {username} > ')

# Laço que se repete até que seja selecionada a opção "k" para sair do programa.
while True:
    user_input = input('\nInício > Digite "c" para CRIAR CONTA, "l" para LOGAR EM UMA CONTA ou "k" para SAIR\nInício > ')

    # "c" para CRIAR CONTA - Instacia novo objeto da classe Account
    if user_input.lower() == 'c':
        # Laço que se repete até que o nome de usuário escolhido seja único.
        while True: 
            user_input = input('\nInício > Registro > Escolha um NOME DE USUÁRIO: ')
            username = user_input
            found_account = False # Variável auxiliar: Representa se a conta foi encontrada. 
            for account in Account.accounts:
                if user_input == account.username:
                    found_account = True  
            if found_account:
                print('Início > Registro > ERROR: Nome de usuário indisponível, experimente usar outro')
                continue  
            break # Quebra o laço infinito, caso o nome de usuário escolhido seja único.
        
        user_input = input('Início > Registro > Escolha uma SENHA FORTE: ')
        password = user_input
        account_to_create = Account(username, password) # Instancia novo objeto na classe Account
        Account.accounts.append(account_to_create)
        selected_account = Account.accounts[-1] # A conta selecionada será a última criada

        # Chama a função que gerencia a conta e saldo de cada usuário.
        use_account(selected_account.username, selected_account)

    # "L" para LOGAR EM UMA CONTA - Seleciona o objeto da classe Account a partir de seus atributos.
    elif user_input.lower() == 'l':
        if Account.accounts:
            user_input = input('\nInício > Login > Digite o NOME DE USUÁRIO: ')
            found_account = False # Variável auxiliar: Representa se a conta foi encontrada.
            for account in Account.accounts:
                if user_input == account.username:
                    selected_account = account
                    found_account = True
                    break
            if not found_account:
                print('Início > Login > ERROR: Usuário não encontrado')
                continue
            for to_try in range(1, 4):
                user_input = input(f'Início > Login > Digite a SENHA do usuário "{selected_account.username}": ')
                if selected_account.password == user_input:
                    print('Início > Login > Login efetuado com sucesso')
                    
                    # Chama a função que gerencia a conta e saldo de cada usuário.
                    use_account(selected_account.username, selected_account)
                    break
                else:
                    if not to_try == 3:
                        print(f'Início > Login > ERROR: Senha incorreta (Tentativas restantes: {3-to_try})')
                    else:
                        print(f'Início > Login > ERROR: Você excedeu o limite de tentativas')
        # Imprime erro, caso não haja pelo menos uma conta criada.    
        else:
            print('Início > ERROR: Ainda não há contas criadas, experimente criar uma')
            
    # "k" para SAIR
    elif user_input.lower() == 'k':
        break
    # Imprime erro, cajo nenhuma opção válida seja digitada ou seja digitado algo por acidente.
    else:
        wrong_option('Início > ')
        
# Caso exista pelo menos uma conta criada, serão impressos os saldos referentes a cada conta.
if Account.accounts:
    print()
    for account in Account.accounts:
        print(f'A conta do usuário "{account.username}" terminou com: R${account.balance}')
    print()
