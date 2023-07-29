# variáveis globais
deposito = 0
saque = 0
extrato = []
saldo = 0
LIMITE_DE_SAQUE = 500
limite_de_saque_diario = 0
loop = True

# mensagem de boas vindas
apresentacao = ' SISTEMA BANCÁRIO '
print()
print(apresentacao.center(60, '*'))
print()

# loop do sistema bancário
while loop:
    # texto menu de opções

    menu =  '''
============================================================
                    Menu de opções:
                    [d] DEPOSITO
                    [s] SAQUE
                    [e] EXTRATO
                    [f] FINALIZAR
                    '''
    # exibir menu de opções
    print(menu)

    # entrada de parâmetro do usuário
    opcao = input('Escolha uma opção:').lower()
    print('=' * 60)

    # Menu de opções = DEPOSITO
    if opcao == 'd':
        try:
            print()
            # entrada de parâmetro do usuário
            deposito = float(input('Digite o valor de deposito: '))

            # tomada de decisão (regra de negócio)
            if deposito <= 0:
                print('Deposito NÃO realizado, deposito menor ou igual a R$:0.00.')
            else:
                saldo += deposito
                texto = str(f'Deposito = R$:{deposito:.2f}')
                extrato.append(texto)
                print('Deposito realizado com sucesso!!!')

        # mensagem de erro para valores não validos
        except Exception as erro:
            print(f'\nErro de operação => ({erro})')
            print('Verifique o valor digitado!!!')

    # Menu de opções = SAQUE
    elif opcao == 's':
        try:
            print()
            # entrada de parâmetro do usuário
            saque = float(input('Digite o valor de saque: '))

            # tomada de decisão (regra de negócio)
            if limite_de_saque_diario >= 3:
                print('Saque NÃO realizar, já foi atingido limite diário de (3 saques diário).\n')
            elif saque > LIMITE_DE_SAQUE:
                print('Saque NÃO realizar seu limite para saque é de R$:500,00.\n')
            elif saque > saldo:
                print('Saque NÃO realizar, saldo insuficiente.\n')
            elif saque <= 0:
                print('Saque NÃO realizar, saque menor ou igual a R$:0.00.\n')
            else:
                limite_de_saque_diario += 1
                saldo -= saque
                texto = str(f'  Sacado = R$:{saque:.2f}')
                extrato.append(texto)
                print('Saque realizado com sucesso!!!')

        # mensagem de erro para valores não validos
        except Exception as erro:
            print(f'\nErro de operação => ({erro})')
            print('Verifique o valor digitado!!!')

    # Menu de opções = EXTRATO
    elif opcao == 'e':
        print()
        print(' Extrato bancário '.center(25, '#'))
        print('-' * 25)
        if extrato == []:
            print('Saldo total R$:0.00')
        else:
            for i in extrato:
                print(i)
            print('-' * 25)
            print(f'Saldo total R$:{saldo:.2f}')

    # Menu de opções = FINALIZAR
    elif opcao == 'f':
        # opções para encerra loop e finalizar programa
        while True:
            # entrada de parâmetro do usuário
            loop = input('\nDeseja finalizar Sim = [s] ou Não = [n]:').lower()

            # resposta para usuário
            if loop == 's':
                loop = False
                break
            elif loop == 'n':
                loop = True
                break
            else:
                # mensagem de erro caso  a resposta não seja Sim [s] ou Não [n]
                loop = True
                print('\nOpção invalida!!! \nDigite [s] para FINALIZAR ou [n] RETORNAR')
    else:
        # caso usuário digite qualquer opção não existente no "Menu de opções" 
         print('\nOpção invalida, digite a letra correspondente ao menu de opções:')

# mensagem final para usuário
print('\nSistema finalizado com sucesso!!!\n')
