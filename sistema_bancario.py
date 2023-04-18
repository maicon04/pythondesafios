menu = """
  [d] Depositar
  [s] Sacar
  [e] Extrato
  [q] Sair
 => """

saldo = 0
limite = 500
extrato = f"Saldo inicial R$ {saldo:.2f}\n"
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    #1 - Depósitar
    if opcao == 'd':
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou. O valor informado é inválido. Refaça o depósito!!")

    #2 - Sacar
    elif opcao == 's':

        valor = float(input("Informe o valor do saque: "))

        saldo_excedido = valor > saldo
        limite_excedido = valor >= limite
        saques_execedido = numero_saques >=  LIMITE_SAQUES

        if limite_excedido:
            print(f"O limite por saque é de R$ {limite}")
        elif saques_execedido:
            print(f"O número de saques efetuados no dia já superou o limite. Limite de saques : {LIMITE_SAQUES} saques efetuados {numero_saques}")
        elif saldo_excedido:
            print("Sem saldo para realizar saques.")
        else:
            numero_saques +=1
            print(f"Saque efetuado com sucesso. Valor do Saque R$ {valor}")
            saldo -= valor1
            extrato += f"Saque: R$ {valor:.2f}\n"

    #3 - Extrato
    elif opcao == 'e':
        print("\n=========================== EXTRATO ===========================")
        print("Não foram encontradas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=================================================================")
    
    #4 - Sair
    elif opcao == 'q':
        break
    else:
        ("Opção inválida. Por favor, selecione uma das opções possíveis.")

