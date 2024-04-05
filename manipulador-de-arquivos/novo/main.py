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
        opcoes_menu = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

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
                # será "[0, 1, 2, 3]"
                opcoes_numericas_possiveis = list(range(len(dados_arquivo_de_texto)))

                novo_dado = ''


                posicao_da_linha_a_ser_modificada = 0 # 0 = False


                # 0 = False
                while not posicao_da_linha_a_ser_modificada:
                    
                    # usuário escolhe a linha do arquivo de texto a ser modificada.Como a primeira linha da lista de opções dispoíveis é igual a 0, logo a escolha que de linha que o usuário fizer deve ser subtraído 1 para então dar "match"
                    posicao_da_linha_a_ser_modificada = (leiaInt("Selecione uma opção: ") - 1)


                    # verifica se a escolha de linha que o usuário fez está na lista de opções possíveis
                    if posicao_da_linha_a_ser_modificada in opcoes_numericas_possiveis:

                        break


                    
                    # posicao_da_linha_a_ser_modificada igual a 0: volta pro laço while
                    else:


                        posicao_da_linha_a_ser_modificada = 0 # 0 = False


                # Lê o novo dado a substituir o velho
                while True:

                    novo_dado = str(input("Novo dado a substituir o velho: ")).strip()



                    if novo_dado:

                        break

                # chama o método de editar arquivo, editando assim o arquivo.A variável "novos_dados" recebe o retorno dos novos do arquivo de texto após ele ser modifcado
                novos_dados = arquivo_texto1.editar_arquivo(posicao_da_linha_a_ser_modificada, novo_dado)

                # grava os novos dados no arquivo de texto
                arquivo_texto1.grava_alteracoes_no_arquivo_de_texto(novos_dados)            


            # Excluir linha
            elif escolhaUsuario == 4:

                
                # obtém uma lista dos índices da lista retornada a partir dos dados do arquivo de texto.

                #exemplo: há 4 linhas no arquivo
                # nesse caso, o conteúdo da variável "opcoes_numericas_do_arquivo"
                # será "[0, 1, 2, 3]"
                posicoes_numericas_do_arquivo =  list(range(len(arquivo_texto1.retorna_lista_de_dados_do_arquivo_de_texto())))


                # exibe todo o conteúdo do arquivo
                arquivo_texto1.lerArquivo()



                #usuário deve escolher a posição da linha a ser removida
                while True:


                    posicao_da_linha_a_ser_removida = leiaInt("Posição da linha a ser removida: ") - 1


                    if posicao_da_linha_a_ser_removida in posicoes_numericas_do_arquivo:


                        break


                    print("\033[1;31mOpção inexistente.Tente novamente.\033[m")


                # chama o método para excluir a linha especificado do arquivo.Após, é retornado os novos dados do arquivo de texto.
                novos_dados = arquivo_texto1.excluir_linha_do_arquivo_de_texto(posicao_da_linha_a_ser_removida)

                # com os novos dados em mãos, os dados são gravados no arquivo de texto
                arquivo_texto1.grava_alteracoes_no_arquivo_de_texto(novos_dados)

                

            # limpa/apaga dados do arquivo de texto
            elif escolhaUsuario == 5:

                
                # mensagem de aviso
                while True:


                    print("\033[1;33;41mATENÇÃO!\033[m")

                    sleep(1.5)

                    print(f'\033[1;43mTodos os dados do arquivo "{arquivo_texto1.nome}" serão apagados.\033[m')

                    sleep(2)


                    # escolha do usuário
                    escolhaUsuario = str(input("\033[1;43mProceder mesmo assim [S/N]? \033[m")).strip().upper()[0]


                    if escolhaUsuario in ["S", "N"]:

                        break


                    print("\033[1;31mPor favor, selecione uma opção válida.\033[m")


                # usuário optou por excluir os dados
                
                if escolhaUsuario == "S":
                    

                    # limpa o arquivo e retorna uma lista vazia.Assim, a lista vazia é gravada no arquivo de texto

                    dados_vazios = arquivo_texto1.limpar_arquivo()


                    arquivo_texto1.grava_alteracoes_no_arquivo_de_texto(dados_vazios)


                # usuário optou por não excluir os seus dados
                else:



                    print("A exclusão dos dados do arquivo foi cancelada.")



            # renomear arquivo
            if escolhaUsuario == 6:


                
                # lê e valida o novo nome do arquivo
                while True:


                    novo_nome = str(input("Novo nome do arquivo de texto: ")).strip()


                    if novo_nome:

                        break


                    print("\033[1;31mO nome do arquivo não pode ficar em branco.\033[m")


                # armazena o velho nome do arquivo para ser usado 
                velho_nome_do_arquivo = arquivo_texto1.nome


                # nome do objeto mudou para o novo nome
                arquivo_texto1.nome = novo_nome 


                # chama o método que renomeará o arquivo de texto                
                arquivo_texto1.renomeia_arquivo_de_texto(velho_nome_do_arquivo, novo_nome)




            
            # apagar arquivo
            elif escolhaUsuario == 7:



                # aviso dado ao usuário informando que ele está prestes a excluir o arquivo
                print("\033[1;33;41mATENÇÃO!\033[m")
                sleep(1.5)

                print(f'\033[1;43mVocê está prestes a apagar o arquivo "{arquivo_texto1.nome}".\033[m')


                sleep(2)


                # pergunta e valida se usuário quer continuar a exclusão de qualquer forma
                while True:


                    perguntaUsuario = str(input("Proceder mesmo assim [S/N]? ")).strip().upper()[0]


                    if perguntaUsuario in ["S", "N"]:

                        break


                    print("\033[1;31mOpção inválida.Tente novamente.\033[m")


                # se o usuário assim desejar em excluir o arquivo, então ele é excluído
                if perguntaUsuario == "S":

                    arquivo_texto1.apagarArquivoDeTexto()



            # copiar para um novo arquivo
            elif escolhaUsuario == 8:


                pasta_criada = arquivo_criado = False


                # retorna uma lista com os dados do arquivo de texto principal
                dados_do_arquivo_de_texto_principal = arquivo_texto1.retorna_lista_de_dados_do_arquivo_de_texto()


                # enquanto a pasta não é criada, é exigido que o usuário digite o nome da pasta que conterá o arquivo, ao mesmo tempo em que o nome da pasta é validada e verificada se a pasta já existe no diretório
                while not pasta_criada:


                    while True:


                        nome_da_pasta = str(input("Nome da pasta onde ficará o novo arquivo: ")).strip()


                        nome_e_valido = ArquivoDeTexto.valida_nome_da_pasta(nome_da_pasta)


                        if nome_e_valido:

                            break


                        print("\033[1;31mNome de pasta inválido.Por favor, tente novamente.\033[m")


                    # verifica se a pasta especificada já existe
                    pasta_ja_existe = ArquivoDeTexto.verifica_se_o_nome_da_pasta_especificado_ja_existe_no_diretorio(nome_da_pasta)


                    # a pasta ainda não existir, logo ela é criada
                    if not pasta_ja_existe:
                    
                        ArquivoDeTexto.criar_pasta_para_o_arquivo(nome_da_pasta)

                        pasta_criada = True

                    
                    # a pasta já existe
                    else:


                        print("\033[1;31mA pasta especificada já existe.Por favor, escolha outro nome de pasta.\033[m")



                # enquanto o arquivo não é criado, o leia, o valide e verifique se o mesmo existe
                while not arquivo_criado:

                    nome_do_arquivo = str(input("Nome do arquivo a ser copiado: ")).strip()


                    novo_nome_arquivo = ArquivoDeTexto.valida_nome_do_arquivo(nome_do_arquivo)


                   

                    # cria o arquivo de cópia
                    ArquivoDeTexto.cria_arquivo_de_copia(nome_da_pasta, novo_nome_arquivo)


                    # o arquivo foi criado
                    arquivo_criado = True


                # pega os dados recebido (em formato de lista) e converte para string
                dados_do_arquivo_principal_formatados_em_string = arquivo_texto1.formata_dados_recebidos_do_arquivo_principal_para_string(dados_do_arquivo_de_texto_principal)
                
                # copia os dados para  orquivo principal
                arquivo_texto1.copia_dados_do_arquivo_principal_para_o_arquivo_de_copia (nome_da_pasta, novo_nome_arquivo, dados_do_arquivo_principal_formatados_em_string)



            # copiar dados para um arquivo existente
            elif escolhaUsuario == 9:

                nome_da_pasta_existe = False

                nome_da_pasta = ''
                

                # retorna uma lista das linhas/dados do arquivo de texto principal
                dados_do_arquivo_de_texto_principal = arquivo_texto1.retorna_lista_de_dados_do_arquivo_de_texto()


                # formata as linhas/dados  do arquivo principal para string
                dados_do_arquivo_de_texto_principal_formatados = arquivo_texto1.formata_dados_recebidos_do_arquivo_principal_para_string(dados_do_arquivo_de_texto_principal)


                # exibe as pastas do diretório atual
                ArquivoDeTexto.exibe_pastas_do_diretório_atual()


                # verifiva se a pasta contendo o arquivo de cópia realmente existe
                while not nome_da_pasta_existe:

                    nome_da_pasta = str(input("Nome da pasta: ")).strip()

                    pasta_existe = arquivo_texto1.verifica_se_o_nome_da_pasta_especificado_ja_existe_no_diretorio(nome_da_pasta)

                    
                    # a pasta existe de fato, saia do loop
                    if pasta_existe:

                        break
                    
                    # a pasta não existe, retorne para o loop
                    print("\033[1;31mA pasta não existe.Tente novamente com uma pasta existente\033[m")


                #obtém uma lista dos arquivos da pasta que contém o arquivo a ser copiado para (possivelmente, só há um arquivo na pasta, que é o arquivo a ser copiado)
                nome_do_arquivo =  os.listdir(f'novo/{nome_da_pasta}/')

                # pega o único nome de arquivo da lista, que é o arquivo a ter dados copiados nele e que terá os dados copiados para si
                nome_do_arquivo = nome_do_arquivo[0]

                
                # chama o método que copia os dados do arquivo principal para o arquivo de cópia
                arquivo_texto1.copia_dados_do_arquivo_principal_para_o_arquivo_de_copia(nome_da_pasta, nome_do_arquivo, dados_do_arquivo_de_texto_principal_formatados)
                    





            # sair
            elif escolhaUsuario == 10:

                exit(0)    

        