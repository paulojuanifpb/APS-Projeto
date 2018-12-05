from model.Classes import Pessoa
from model.Classes import Bebida
from model.Classes import Cliente
from model.Classes import Gerente
import sqlite3



#criação da conexão e do Banco de Dados
conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()


def menuPrincipal():
    print("1- Sou Cliente")
    print("2- Sou Gerente")
    print("0- SAIR")

def menuCliente():
    print("1- ENTRAR")
    print("2- CADASTRAR")
    print("0- SAIR")

def funcaoCliente():
    print("1- FAZER UMA COMPRA")
    print("0- SAIR")

def menuGerente():
    print("1- ENTRAR")
    print("2- CADASTRAR")
    print("0- SAIR")

def funcaoGerente():
    print("1- CADASTRAR BEBIDA")
    print("0- SAIR")

def bebidas():
 print("1-> Fardo de Cerveja __________________________R$15,00")
 print("2-> Fardo de Refrigerante __________________________R$10,00")
 print("3-> Fardo de Cachaça __________________________R$18,00")
 print("4-> Fardo de Vinho Branco __________________________R$19,00")
 print("5-> Fardo de Conhaque __________________________R$22,00")
 print("6-> Fardo de Whisky __________________________R$24,00")
 print("7-> Fardo de Tequila __________________________R$23,00")
 print("8-> Fardo de Champanhe __________________________R$25,00")
 print("9-> Fardo de Vodka __________________________R$17,00")
 print("10-> Fardo de Água __________________________R$13,00")

#variáveis globais

nome = ""
endereco = ""
rg = 0
email = ""
telefone = 0
senha = ""
valor = 0.0
quantidade = 0
#Criando o objeto Cliente, Gerente, Bebida e Distribuidora
c1 = Cliente(nome, endereco, rg, email, telefone, senha)
g1 = Gerente(nome, endereco, rg, email, telefone, senha)
b1 = Bebida (nome, valor, quantidade)


menuPrincipal()

op = int(input("Escolha:\n"))
if(op == 1):
    menuCliente()
    op2 = int(input("Escolha:\n"))
    while(op2 != 0):
        if( op2 == 1):
         cliente = int(input("Digite o Seu RG:\n"))
         password = str(input("Digite a sua Senha:\n"))
         if(cliente == c1.rg and password == c1.senha ):
            if( op2 == 1):

                funcaoCliente()
                op4 = int(input("Escolha:\n"))
                while(op4 != 0):
                        if(op4 == 1):
                            bebidas()
                            op5 = int(input("Digite o Numero Correspondente à Bebida:\n"))
                            NBebidas = int(input("Quantos Fardos:\n"))
                            if(op5 == 1):

                                print("Sua Compra Ficou no Valor:\n")
                                x = NBebidas*15
                                print(x, "Reais")
                                cpf = int(input("Numero do CPF:\n"))
                                NCartao = int(input("Numero do Cartão:\n"))
                                print("Confirmar Compra 1->Sim, 0-> Não:\n ")
                                op6 = int(input("Escolha:\n"))
                                if(op6 == 1):
                                 print("Compra Concluida Com Sucesso")
                                if(op6 == 1):
                                    op4 = int(input("Deseja Fazer Outra Compra: 1-> SIM  0 -> NÃO\n"))
                                else:
                                    op2 = 0


                            elif(op5 == 2):


                                print("Sua Compra Ficou no Valor:\n")
                                x1 = NBebidas*10
                                print(x1, "Reais")
                                cpf = int(input("Numero do CPF:\n"))
                                NCartao = int(input("Numero do Cartão:\n"))
                                print("Confirmar Compra 1->Sim, 0-> Não:\n ")
                                op6 = int(input("Escolha:\n"))
                                if(op6 == 1):
                                 print("Compra Concluida Com Sucesso")
                                if(op6 == 1):
                                    op4 = int(input("Deseja Fazer Outra Compra: 1-> SIM  0 -> NÃO\n"))
                                else:
                                    op4 = 0
                                    op2 = 0


                            elif(op5 == 3):


                                print("Sua Compra Ficou no Valor:\n")
                                x2 = NBebidas*18
                                print(x2, "Reais")
                                cpf = int(input("Numero do CPF:\n"))
                                NCartao = int(input("Numero do Cartão:\n"))
                                print("Confirmar Compra 1->Sim, 0-> Não:\n ")
                                op6 = int(input("Escolha:\n"))
                                if(op6 == 1):
                                 print("Compra Concluida Com Sucesso")
                                if(op6 == 1):
                                    op4 = int(input("Deseja Fazer Outra Compra: 1-> SIM  0 -> NÃO\n"))
                                else:
                                    op4 = 0
                                    op2 = 0


                            elif(op5 == 4):

                                print("Sua Compra Ficou no Valor:\n")
                                x3 = NBebidas*19
                                print(x3, "Reais")
                                cpf = int(input("Numero do CPF:\n"))
                                NCartao = int(input("Numero do Cartão:\n"))
                                print("Confirmar Compra 1->Sim, 0-> Não:\n ")
                                op6 = int(input("Escolha:\n"))
                                if(op6 == 1):
                                 print("Compra Concluida Com Sucesso")
                                if(op6 == 1):
                                    op4 = int(input("Deseja Fazer Outra Compra: 1-> SIM  0 -> NÃO\n"))
                                else:
                                    op4 = 0
                                    op2 = 0


                            elif(op5 == 5):

                               print("Sua Compra Ficou no Valor:\n")
                               x4 = NBebidas*22
                               print(x4, "Reais")
                               cpf = int(input("Numero do CPF:\n"))
                               NCartao = int(input("Numero do Cartão:\n"))
                               print("Confirmar Compra 1->Sim, 0-> Não:\n ")
                               op6 = int(input("Escolha:\n"))
                               if(op6 == 1):
                                print("Compra Concluida Com Sucesso")
                               if(op6 == 1):
                                    op4 = int(input("Deseja Fazer Outra Compra: 1-> SIM  0 -> NÃO\n"))
                               else:
                                    op4 = 0
                                    op2 = 0


                            elif(op5 == 6):


                                print("Sua Compra Ficou no Valor:\n")
                                x5 = NBebidas*24
                                print(x5, "Reais")
                                cpf = int(input("Numero do CPF:\n"))
                                NCartao = int(input("Numero do Cartão:\n"))
                                print("Confirmar Compra 1->Sim, 0-> Não:\n ")
                                op6 = int(input("Escolha:\n"))
                                if(op6 == 1):
                                 print("Compra Concluida Com Sucesso")
                                if(op6 == 1):
                                    op4 = int(input("Deseja Fazer Outra Compra: 1-> SIM  0 -> NÃO\n"))
                                else:
                                    op4 = 0
                                    op2 = 0


                            elif(op5 == 7):


                                print("Sua Compra Ficou no Valor:\n")
                                x6 = NBebidas*23
                                print(x6, "Reais")
                                cpf = int(input("Numero do CPF:\n"))
                                NCartao = int(input("Numero do Cartão:\n"))
                                print("Confirmar Compra 1->Sim, 0-> Não:\n ")
                                op6 = int(input("Escolha:\n"))
                                if(op6 == 1):
                                 print("Compra Concluida Com Sucesso")

                                if(op6 == 1):
                                    op4 = int(input("Deseja Fazer Outra Compra: 1-> SIM  0 -> NÃO\n"))
                                else:
                                    op4 = 0
                                    op2 = 0

                            elif(op5 == 8):


                                print("Sua Compra Ficou no Valor:\n")
                                x7 = NBebidas*25
                                print(x7, "Reais")
                                cpf = int(input("Numero do CPF:\n"))
                                NCartao = int(input("Numero do Cartão:\n"))
                                print("Confirmar Compra 1->Sim, 0-> Não:\n ")
                                op6 = int(input("Escolha:\n"))
                                if(op6 == 1):
                                 print("Compra Concluida Com Sucesso")
                                if(op6 == 1):
                                    op4 = int(input("Deseja Fazer Outra Compra: 1-> SIM  0 -> NÃO\n"))
                                else:
                                    op4 = 0
                                    op2 = 0

                            elif(op5 == 9):


                               print("Sua Compra Ficou no Valor:\n")
                               x8 = NBebidas*17
                               print(x8, "Reais")
                               cpf = int(input("Numero do CPF:\n"))
                               NCartao = int(input("Numero do Cartão:\n"))
                               print("Confirmar Compra 1->Sim, 0-> Não:\n ")
                               op6 = int(input("Escolha:\n"))
                               if(op6 == 1):
                                 print("Compra Concluida Com Sucesso")
                               if(op6 == 1):
                                 op4 = int(input("Deseja Fazer Outra Compra: 1-> SIM  0 -> NÃO\n"))
                               else:
                                    op4 = 0
                                    op2 = 0

                            elif(op5 == 10):


                                print("Sua Compra Ficou no Valor:\n")
                                x9 = NBebidas*13
                                print(x9, "Reais")
                                cpf = int(input("Numero do CPF:\n"))
                                NCartao = int(input("Numero do Cartão:\n"))
                                print("Confirmar Compra 1->Sim, 0-> Não:\n ")
                                op6 = int(input("Escolha:\n"))
                                if(op6 == 1):
                                 print("Compra Concluida Com Sucesso")
                                if(op6 == 1):
                                    op4 = int(input("Deseja Fazer Outra Compra: 1-> SIM  0 -> NÃO\n"))
                                else:
                                    op4 = 0
                                    op2 = 0



            else:
                print("Dados inválidos")
                op2 = 0


        if( op2 == 2):
            c1.nome = str(input("Digite o seu nome:\n"))
            c1.endereco = str(input("Digite o seu endereço:\n"))
            c1.email = str(input("Digite o seu email:\n"))
            c1.telefone = int(input("Digite o seu telefone:\n"))
            c1.rg = int(input("Digite o seu RG:\n"))
            c1.senha = str(input("Digite o sua Senha:\n"))
            # inserindo dados na tabela Clientes
            cursor.execute("""
            INSERT INTO clientes (nome, endereco, email, fone, Rg,  senha)
            VALUES (?,?,?,?,?,?)
            """,(c1.nome, c1.endereco, c1.email, c1.telefone, c1.rg, c1.senha))
            print("CADASTRADO COM SUCESSO")
            menuCliente()
            op2 = int(input("Escolha:"))

elif(op == 2):
    menuGerente()
    op2 = int(input("Escolha:\n"))
    while(op2 != 0):
        if( op2 == 1):
            gerente = int(input("Digite o Seu RG:\n"))
            password = str(input("Digite a sua Senha:\n"))
            if(gerente == g1.rg and password == g1.senha ):
                funcaoGerente()
                op3 = int(input("Escolha:\n"))
                while (op3 != 0):
                    if(op3 == 1):
                        b1.nome = str(input("Nome Da Bebida:\n"))
                        b1.valor = float(input("Valor:\n"))
                        b1.quantidade = int(input("Quantidade:\n"))
                        # inserindo dados na tabela Bebidas
                        cursor.execute("""
                        INSERT INTO bebidas (nome, valor, quantidade)
                        VALUES (?,?,?)
                        """,(b1.nome, b1.valor, b1.quantidade))
                        print("CADASTRADO COM SUCESSO")
                        funcaoGerente()
                        op2 = int(input("Escolha:"))
                        op3 = op2


        if( op2 == 2):
            g1.nome = str(input("Digite o seu nome:\n"))
            g1.endereco = str(input("Digite o seu endereço:\n"))
            g1.email = str(input("Digite o seu email:\n"))
            g1.telefone = int(input("Digite o seu telefone:\n"))
            g1.rg = int(input("Digite o seu RG:\n"))
            g1.senha = str(input("Digite o sua Senha:\n"))
            # inserindo dados na tabela Gerentes
            cursor.execute("""
            INSERT INTO gerentes (nome, endereco, email, fone, Rg,  senha)
            VALUES (?,?,?,?,?,?)
            """, (g1.nome, g1.endereco,g1.email,g1.telefone, g1.rg, g1.senha))
            print("CADASTRADO COM SUCESSO")
            menuGerente()
            op2 = int(input("Escolha:"))






conn.commit()

conn.close()






