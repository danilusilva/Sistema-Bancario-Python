menu = """
        ***SEJA BEM-VINDO AO BANCO DANLET***
        Selecione a opção desejada:

         [1] DEPOSITAR 
         [2] SACAR
         [3] EXTRATO BANCÁRIO
         [0] FINALIZAR OPERAÇÃO

         => """

saldo = 0
limite = 500
extrato_des = ''
saques_realizados = 0
depositos_realizados = 0
LIMITE_SAQUE = 3

def depositar():
    valor_depositar = float(input("Insira o valor a ser depositado:"))
    global saldo
    global depositos_realizados
    global extrato_des
    if valor_depositar > 0:
     saldo += valor_depositar
     depositos_realizados = depositos_realizados + 1
     extrato_des += f'Depósito:R$ {valor_depositar:.2f}\n'
     print(f"R${valor_depositar} foram depositados com sucesso!")

    else:
        print("Valor inválido!")

def sacar():
     global saldo
     global saques_realizados
     global extrato_des
     valor_sacar = float(input("Insira o valor a ser sacado:"))

     if saques_realizados >= LIMITE_SAQUE:
         print("Você atingiu o limite de saques diário, volte amanhã!")
         return
     
     if valor_sacar > saldo:
        print("Você não tem saldo para sacar esse valor, consulte o extrato para saber o seu saldo.")
        return
     
     if valor_sacar > limite:
        print(f"O limite para saque é R${limite}, tente novamente com um valor igual ou menor ao limite!")
        return
     
     if valor_sacar > 0:
        saldo -= valor_sacar
        saques_realizados = saques_realizados + 1
        extrato_des += f'Saque: R${valor_sacar:.2f}\n'
        print(f"R${valor_sacar} foram sacados com sucesso!")

     else:
         print("Valor inválido!")


     

def extrato():
    global saldo
    print(f"O saldo na conta é:{saldo:.2f}\n")
    print("Não há movimentações" if not extrato_des else extrato_des)


     

while True:
    
    
    opcao = int(input(menu))

    if opcao == 1:
        print("Depositar")
        depositar()
    
    elif opcao == 2:
        print("Sacar")
        sacar()
        
    elif opcao == 3:
        print("Extrato Bancário")
        extrato()
    
    elif opcao == 0:
        print("Finalizando operação, volte sempre!")
        break
    
    else:
        print("Não foi possível encontrar a opção desejada, tente novamente.")



