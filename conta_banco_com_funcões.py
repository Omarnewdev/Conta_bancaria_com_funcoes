import sys


menu_cuenta = """

[d] Depositar
[s] Sacar
[e] Extrato 
[q] Sair

=> """

menu_inicio = """
[nu] Novo Usuario
[imu] Printar lista de Usuarios
[eu] Entrar Usuario
[x] salir

=>"""

menu_usuario = """
[cc] Criar Conta
[ec] entrar Conta

[usar conta]=>

"""



def printar_usuarios(lista_de_usuarios:dict):
    if len(lista_de_usuarios) <= 0:
        print("Não tem nehum usuario cadastrado")
    else:
        for cpf,usuario in lista_de_usuarios.items():
            nome,data,endereco,contas = usuario
            print(f"O usuario {nome} com o cpf {cpf} nasceu {data} e mora em {endereco} tem {len(contas)} contas registradas")




def criar_usuario(nome, data_nascimento, cpf, enderco, lista_de_usuarios ):
    #Primeramente vamos ver se existe algum usuario como o mesmo cpf
    if cpf in lista_de_usuarios:
        print("Existe um usuário com o CPF fonecido")
        return
    else:
        contas_correntes = []
        nuevo_usuario = [nome,data_nascimento,enderco,contas_correntes]
        lista_de_usuarios[cpf] = nuevo_usuario
        print("Novo Usuario Criado")

def entrar_usuario(lista_de_usuarios,cpf):
    if cpf in lista_de_usuarios:
        return True,lista_de_usuarios[cpf]
    else:
        print("Não existe nehum usuário com esse cpf")
        return False,[]
        
def entrar_conta(usuario_atual,numero_conta):
    conta = usuario_atual[3]
    if len(conta) == 0:
        print("O usuario não tem comtas")
    else:
        print("hola")

def criar_conta(usuario_atual):
    saldo = 0
    nova_conta = [int("0"+str(len(usuario_atual[3]))),saldo]
    usuario_atual[3].append(nova_conta)

def printar_contas(usuario_atual):
    if len(usuario_atual[3]) == 0:
        print("Nao tem comtas")
    else:
        for conta in usuario_atual[3]:
            print(f' {conta[0]} com saldo {conta[1]} \n')

def saque(*,valor,conta_atual):
    conta_atual[1] -= valor


def deposito(valor,conta_atual):
    conta_atual[1] += valor

def extrato(conta_atual):
    print("\n================ EXTRATO ================")
    print(f"\nSaldo: R$ {conta_atual[1]:.2f}")
    print("==========================================")



saldo = 0
limite = 500
lista_de_usuarios = dict()


while True:
    usuario_atual = []
    saques = 0 # Cada vez que a gente troque de usuário o limite de saque zerea
    while True:    
        op= input(menu_inicio)
        
        if op == "nu":
            nome = input("Insira o nome do novo usuário: ")
            data_nascimento = input("Insira a data de nascimento do Usuario [dd/mm/yyyy]: ")
            endereco = input("Insira o endereco do Usuario: logradouro, nro - bairro - cidade/sigla estado ")
            cpf = input("Insira o cpf do Usuario: ")
            # Estou fazendo isto para que só fique uma cadena de números
            re_cpf = "".join([ele for ele in cpf if ele.isdigit()])
            print("{re_cpf} \n")
            criar_usuario(nome,data_nascimento,re_cpf,endereco,lista_de_usuarios)

        elif op == "imu":
            printar_usuarios(lista_de_usuarios)

        elif op == "eu":
            cpf = input("Insira o cpf da conta =>")
            existe,usuario_atual = entrar_usuario(lista_de_usuarios=lista_de_usuarios,cpf=cpf)
            if existe:
                print("Entrando na conta do usário com cpf: {cpf}")
                break
            else:
                print("Usuario não encontrado")        
            
            
            
        elif op == "x":
            sys.exit()


    while True:
        op = input(menu_usuario)
        if op == "cc":
            criar_conta(usuario_atual=usuario_atual)
        elif op == "ec":
            printar_contas(usuario_atual)
            escolher = input("Escolha qual numero de conta quer entrar")
            if len(usuario_atual[3])-1 < int(escolher):
                print("Insira corretamente o numero de conta")
            else:
                conta_atual = usuario_atual[3][int(escolher)]
                break
        

    while True:

        opcao = input(menu_cuenta)

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            if valor>0:
                deposito(valor,conta_atual)
            else:
                print("Insira um valor valido")

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            if valor> limite:
                print("O limite do saque é 500 ")
            elif saques>3:
                print("Passou o limite de saques por dia")
            elif conta_atual[1]< valor:
                print("Nao tem o saldo suficiente")
            else:
                saque(valor=valor,conta_atual=conta_atual)
                saque+=1

        elif opcao == "e":
            extrato(conta_atual)

        elif opcao == "q":
            
            break
            
            

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")