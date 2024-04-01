from classes import *
from funcs import *
import os
from time import sleep
from sys import exit



while True:

    

    # verifica se há arquivos no diretório "novo/arquivo de texto/"
    if not os.listdir("novo/arquivo de texto"):
        
        nomeDoArquivo = ''

        # enquanto não for informado um nome, o usuário receberá um input de dados pedindo a ele que digite o nome do arquivo
        while not nomeDoArquivo:

            nomeDoArquivo = str(input("Nome do arquivo: ")).strip()



        # cria o objeto arquivo_texto1, que automaticamente cria o arquivo de acordo com o nome
        arquivo_texto1 = ArquivoDeTexto(nomeDoArquivo)

    # o arquivo já existia no diretório "novo/arquivo de texto/"
    else:

        # obtém uma lista dos arquivos presentes no diretório "novo/arquivo de texto".O primeiro nome de arquivo é pego por padrão.
        nomeDoArquivo = os.listdir("novo/arquivo de texto")[0]

        #cria o objeto arquivo_texto1, que automaticamente cria o arquivo de acordo #com o nome
        arquivo_texto1 = ArquivoDeTexto(nomeDoArquivo)


    # enquanto o arquivo existir, o programa é executado
    while arquivo_texto1.arquivo_existe():

        # opções do menu
        opcoes_menu = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        # exibe o menu
        menu()


        # nesse bloco desse while, a função dele é validar a escolha que o usuário fazer
        while True:


            escolhaUsuario = leiaInt("Sua escolha: ")


            if escolhaUsuario in opcoes_menu:

                break

            print("\033[1;31mOpção inválida.Tente novamente.\033[m")


        # inserir dados no arquivo
        if escolhaUsuario == 1:
            

            linhaDeTexto = ''


            # enquanto o nome do arquivo for vazio, o input de dados  continuará sendo executado
            while len(linhaDeTexto) == 0:
                linhaDeTexto = str(input("Linha de texto a ser inserida: ")).strip()


            # adiciona a linha de texto ao arquivo
            arquivo_texto1.adicionar_linha_de_texto(linhaDeTexto)
            

        # se o arquivo estiver vazio (sem conteúdo nele) e o usuário optar por uma das opções (ler, modificar, excluir, limpar), será exibido a mensagem "arquivo vazio!" a ele
        if arquivo_texto1.arquivo_vazio() and escolhaUsuario in [2, 3, 4, 5]:

            print("\033[1;33mArquivo vazio!\033[m")


        # O arquivo não está vazio e/ou usuário não selecionou nenhuma das opções 2, 3, 4, 5.
        else:

            
            # ler arquivo
            if escolhaUsuario == 2:


                arquivo_texto1.lerArquivo()



            # editar arquivo
            elif escolhaUsuario == 3:


                arquivo_texto1.lerArquivo()


                dados_arquivo_de_texto = arquivo_texto1.retorna_lista_de_dados_do_arquivo_de_texto()

                # obtém uma lista dos índices da lista retornada a partir dos dados do arquivo de texto.

                #exemplo: há 4 linhas no arquivo
                # nesse caso, o conteúdo da variável "opcoes_numericas_possiveis"
                # será "[1, 2, 3, 4]"
                opcoes_numericas_possiveis = list(range(len(dados_arquivo_de_texto)))

                novo_dado = ''


                posicao_da_linha_a_ser_modificada = 0 # 0 = False


                # 0 = False
                while not posicao_da_linha_a_ser_modificada:

                    posicao_da_linha_a_ser_modificada = (leiaInt("Selecione uma opção: ") - 1)


                    if posicao_da_linha_a_ser_modificada in opcoes_numericas_possiveis:

                        break

                    else:


                        posicao_da_linha_a_ser_modificada = 0 # 0 = False



                while True:

                    novo_dado = str(input("Novo dado a substituir o velho: ")).strip()



                    if novo_dado:

                        break


                novos_dados = arquivo_texto1.editar_arquivo(posicao_da_linha_a_ser_modificada, novo_dado)


                arquivo_texto1.grava_alteracoes_no_arquivo_de_texto(novos_dados)            


            elif escolhaUsuario == 4:


                posicoes_numericas_do_arquivo =  list(range(len(arquivo_texto1.retorna_lista_de_dados_do_arquivo_de_texto())))


                arquivo_texto1.lerArquivo()


                while True:


                    posicao_da_linha_a_ser_removida = leiaInt("Posição da linha a ser removida: ") - 1


                    if posicao_da_linha_a_ser_removida in posicoes_numericas_do_arquivo:


                        break


                    print("\033[1;31mOpção inexistente.Tente novamente.\033[m")


                novos_dados = arquivo_texto1.excluir_linha_do_arquivo_de_texto(posicao_da_linha_a_ser_removida)


                arquivo_texto1.grava_alteracoes_no_arquivo_de_texto(novos_dados)

                


            elif escolhaUsuario == 5:


                while True:


                    print("\033[1;33;41mATENÇÃO!\033[m")

                    sleep(1.5)

                    print(f'\033[1;43mTodos os dados do arquivo "{arquivo_texto1.nome}" serão apagados.\033[m')

                    sleep(2)


                    escolhaUsuario = str(input("\033[1;43mProceder mesmo assim [S/N]? \033[m")).strip().upper()[0]


                    if escolhaUsuario in ["S", "N"]:

                        break


                    print("\033[1;31mPor favor, selecione uma opção válida.\033[m")


                
                if escolhaUsuario == "S":


                    dados_vazios = arquivo_texto1.limpar_arquivo()


                    arquivo_texto1.grava_alteracoes_no_arquivo_de_texto(dados_vazios)


                else:



                    print("A exclusão dos dados do arquivo foi cancelada.")


            if escolhaUsuario == 6:


                

                while True:


                    novo_nome = str(input("Novo nome do arquivo de texto: ")).strip()


                    if novo_nome:

                        break


                    print("\033[1;31mO nome do arquivo não pode ficar em branco.\033[m")


                velho_nome_do_arquivo = arquivo_texto1.nome


                arquivo_texto1.nome = novo_nome

                novo_nome = arquivo_texto1.nome
                
                arquivo_texto1.renomeia_arquivo_de_texto(velho_nome_do_arquivo, novo_nome)





            elif escolhaUsuario == 7:




                print("\033[1;33;41mATENÇÃO!\033[m")
                sleep(1.5)

                print(f'\033[1;43mVocê está prestes a apagar o arquivo "{arquivo_texto1.nome}".\033[m')


                sleep(2)


                while True:


                    perguntaUsuario = str(input("Proceder mesmo assim [S/N]? ")).strip().upper()[0]


                    if perguntaUsuario in ["S", "N"]:

                        break


                    print("\033[1;31mOpção inválida.Tente novamente.\033[m")


                if perguntaUsuario == "S":

                    arquivo_texto1.apagarArquivoDeTexto()



            elif escolhaUsuario == 8:


                pasta_criada = arquivo_criado = False

                dados_do_arquivo_de_texto_principal = arquivo_texto1.retorna_lista_de_dados_do_arquivo_de_texto()


                while not pasta_criada:


                    while True:


                        nome_da_pasta = str(input("Nome da pasta onde ficará o novo arquivo: ")).strip()


                        nome_e_valido = ArquivoDeTexto.valida_nome_da_pasta(nome_da_pasta)


                        if nome_e_valido:

                            break


                        print("\033[1;31mNome de pasta inválido.Por favor, tente novamente.\033[m")


                    pasta_ja_existe = ArquivoDeTexto.verifica_se_o_nome_da_pasta_especificado_ja_existe_no_diretorio(nome_da_pasta)


                    if not pasta_ja_existe:
                    
                        ArquivoDeTexto.criar_pasta_para_o_arquivo(nome_da_pasta)

                        pasta_criada = True

                    
                    else:


                        print("\033[1;31mA pasta especificada já existe.Por favor, escolha outro nome de pasta.\033[m")


                while not arquivo_criado:

                    nome_do_arquivo = str(input("Nome do arquivo a ser copiado: ")).strip()


                    novo_nome_arquivo = ArquivoDeTexto.valida_nome_do_arquivo(nome_do_arquivo)


                   

                    ArquivoDeTexto.cria_arquivo_de_copia(nome_da_pasta, novo_nome_arquivo)

                    arquivo_criado = True

                dados_do_arquivo_principal_formatados_em_string = arquivo_texto1.formata_dados_recebidos_do_arquivo_principal_para_string(dados_do_arquivo_de_texto_principal)
                
                arquivo_texto1.copia_dados_do_arquivo_principal_para_o_arquivo_de_copia (nome_da_pasta, novo_nome_arquivo, dados_do_arquivo_principal_formatados_em_string)





                        
            elif escolhaUsuario == 9:

                exit(0)    

        