# Variables:

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# --------------------------------------------------------------------------------------------------------------
# Functions:

def check_numero(num):
    if num.isnumeric():
        return float(num)

def deposito(saldo, valor_deposito):
    if valor_deposito >= 0:
        saldo += valor_deposito
        return saldo

def saque(saldo, limite, valor_saque):
    if (valor_saque <= limite) and (valor_saque <= saldo):
        return saldo - valor_saque
    
# --------------------------------------------------------------------------------------------------------------
# Main program:

while True:

    opcao = input(menu)

    if opcao == "d": # deposito

        valor_deposito = input("Valor do depósito R$: ")
        valor_deposito = check_numero(valor_deposito)

        if valor_deposito is None:
            print("Insira um valor numérico positvo.")
        else:
            resultado = deposito(saldo, valor_deposito)
            if resultado is None:
                print("Valor de depósito inválido. Insira um valor numerico positivo.")
            else:
                saldo = resultado
                extrato = extrato + f"\n+ R${valor_deposito:.2f}"
                print(f"Depósito realizado. Saldo atual: R${saldo:.2f}")

    elif opcao == "s": # saque

        if numero_saques < LIMITE_SAQUES:

            valor_saque = input("Valor do saque R$: ")
            valor_saque = check_numero(valor_saque)

            if valor_saque is None:
                print("Insira um valor numérico positvo.")
            else:
                resultado = saque(saldo, limite, valor_saque)
                if resultado is None:
                    print("Saque excede R$500.00 ou o valor do saldo.")
                else:
                    saldo = resultado
                    numero_saques += 1
                    extrato = extrato + f"\n- R${valor_saque:.2f}"
                    print(f"Saque realizado. Saldo atual: R${saldo:.2f}")

        else:
            print("Número de saques diários excedido.")

    elif opcao == "e": # extrato

        print("Extrato:\n--------------------------")
        if extrato:
              print(f"{extrato}\nSaldo: R${saldo:.2f}")
        else:
            print(f"Sem movimentações.\nSaldo: R${saldo:.2f}")    

    elif opcao == "q": # sair

        break

    else:

        print("Operação inválida, por favor selecione novamente a operação desejada.")