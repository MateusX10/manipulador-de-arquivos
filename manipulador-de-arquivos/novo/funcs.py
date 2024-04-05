def menu():
    

    print('''Menu de opções:
[ 1 ] - Adicionar linha de texto
[ 2 ] - Ler arquivo
[ 3 ] - Editar arquivo
[ 4 ] - Excluir linha
[ 5 ] - Limpar arquivo
[ 6 ] - Renomear arquivo
[ 7 ] - Excluir arquivo
[ 8 ] - Copiar para um novo arquivo
[ 9 ] - Copiar para um arquivo existente
[ 10 ] - Sair
''')



def menu2():

    print('''Menu de opções:
          
[ 1 ] - Criar arquivo
[ 2 ] - Sair
    ''')



def linha(tamanho=30):

    print("-=" * tamanho)


def titulo(texto):

    print(f"<<< {texto} >>>")





def leiaInt(mensagem):


    from sys import exit


    while True:


        try:


            numero = int(input(mensagem))



        except (NameError, ValueError):


            print("\033[1;31mTivemos um problema com o tipo de dados digitados.\033[m")



        except (KeyboardInterrupt):


            print("\033[1;31mO usuário preferiu não informar os dados.\033[m")

            exit(1)


        except Exception as exp:


            print(f"\033[1;31mOcorreu uma exceção = {exp}\033[m")



        else:


            return numero
        


def perguntaSeUsuarioQuerContinuar():


    while True:


        resposta_usuario = str(input("Continuar [S/N]? ")).strip().upper()[0]


        if resposta_usuario in ["S", "N"]:

            break


        print("\033[1;31mOpção inválida.Por favor, tente novamente.\033[m")


    return resposta_usuario
    