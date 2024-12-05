import os 
os.system("cls")

import random

def adicionarTreinos():
    try:
        while True: 
            nome = input("\033[1;37mNome do treino: \033[m").strip().title()
            if nome.replace(" ", "").isalnum():
                break
            else:
                print("\033[1;31mNome inválido, digite novamente!\033[m")

        while True: 
            print(f"\033[1;37mData do treino: \033[m")
            dia = int(input("\033[1;37m- Dia: \033[m"))
            mes = int(input("\033[1;37m- Mês: \033[m"))
            ano = int(input("\033[1;37m- Ano: \033[m"))

            if 1<= dia <= 31 and 1 <= mes <= 12 and ano > 0:
                break 
            else:
                print("\033[1;31mEntrada inválida, Digite novamente...\033[m")
        
        distanciaPercorrida = f"{int(input("\033[1;37mDistância Percorrida (Km): \033[m"))} km"

        while True:
            print("\033[1;37mTempo de Treino:\033[m")
            hora = int(input("\033[1;37m- Hora(s): \033[m"))
            minutos = int(input("\033[1;37m- Minuto(s): \033[m"))
            segundos = int(input("\033[1;37m- Segundo(s): \033[m"))
            if 0 <= minutos <= 59 and 0 <= segundos <= 59:
                break 
            else: 
                print("\033[1;31mEntrada inválida, Digite novamente...\033[m")

        localizacao = f"{input("\033[1;37mLocalização: \033[m").title().strip()}"

        while True: 
            condClima = f"{(input("\033[1;37mCondições Climáticas: \033[m").title().strip())}"
            if condClima.replace(" ", "").isalpha():
                break
            else:
                print("\033[1;31mEntrada inválida, Digite novamente...\033[m")
        
        with open("registroCorridas.txt", "a", encoding="utf8") as registroCorridas:
            registroCorridas.write(f"\nNome do treino: {nome}\nData: {dia}/{mes}/{ano}\nDistância Percorrida: {distanciaPercorrida}\nTempo: {hora} hora(s) {minutos} minuto(s) {segundos} segundo(s)\nLocalização: {localizacao}\nCondições Climáticas: {condClima}\n\n")

    except ValueError:
        print("\033[1;31m#\033[m" * 50)
        print("\033[1;31mEntrada inválida, Digite novamente...\033[m")
        print("\033[1;31m#\033[m" * 50)

def visualizarTreinos():
    try: 
        while True: 
            print("\033[1;37mFiltrar treinos: \033[m\n\033[1;34m[1- Distância Percorrida]\033[m\n\033[1;36m[2- Tempo]\033[m\n\033[1;31m[3- Voltar]\033[m")
            o = int(input("\033[1;37mQual modo deseja filtar o seu treino?: \033[m"))
            with open("registroCorridas.txt", "r", encoding="utf8") as registroCorridas:
                linhas = registroCorridas.readlines()

            treinoEncontrado = False
            if o == 1:
                distanciaPercorrida = f"{int(input('\033[1;37mDistância Percorrida (Km): \033[m'))} km"
                print()
                for i, linha in enumerate(linhas):
                    if distanciaPercorrida in linha:
                        treinoEncontrado = True
                        print("-" * 20)
                        print(linhas[i-2].strip()) # nome do treino 
                        print(linhas[i-1].strip())  # data
                        print(linha.strip()) # distância percorrida
                        print(linhas[i+1].strip()) # tempo
                        print(linhas[i+2].strip()) # localização 
                        print(linhas[i+3].strip()) # condições climáticas
                        print("-" * 20)
                
                if not treinoEncontrado:
                    print("\033[1;31mTreino não encontrado!\033[m")

            elif o == 2:
                print("\033[1;37mTempo de Treino:\033[m")
                hora = int(input("\033[1;37m- Hora(s): \033[m"))
                minutos = int(input("\033[1;37m- Minuto(s): \033[m"))
                segundos = int(input("\033[1;37m- Segundo(s): \033[m"))
                tempo = f"{hora} hora(s) {minutos} minuto(s) {segundos} segundo(s)"
                print()
                for i, linha in enumerate(linhas):
                    if tempo in linha:
                        treinoEncontrado = True
                        print("-" * 20)
                        print(linhas[i-3].strip()) # nome do treino
                        print(linhas[i-2].strip())  # data
                        print(linhas[i-1].strip()) # distância percorrida
                        print(linha.strip()) # tempo
                        print(linhas[i+1].strip()) # localização 
                        print(linhas[i+2].strip()) # condições climáticas
                        print("-" * 20)

                if not treinoEncontrado: 
                    print("\033[1;31mTreino não encontrado!\033[m")
                print()

            elif o == 3:
                print("\033[1;32mVoltando para o menu principal...\033[m")
                break
            else:
                print("\033[1;31mValor inválido, Digite novamente...\033[m")
            print()
    except ValueError:
        print("\033[1;31m#\033[m" * 50)
        print("\033[1;31mEntrada inválida, Digite novamente...\033[m")
        print("\033[1;31m#\033[m" * 50)

def atualizarTreinos(): 
    try: 
        treinoEncontrado = False
        nome = input("\033[1;37mQual é o nome do treino que deseja modificar? \033[m").title()
        with open("registroCorridas.txt" , "r", encoding="utf8") as registroCorridas:
            linhas = registroCorridas.readlines()

        for i in range(len(linhas)):
            if nome in linhas[i]:
                treinoEncontrado = True
                print("\033[1;31m[1- Nome do treino]\033[m\n\033[1;32m[2- Data do Treino]\033[m\n\033[1;33m[3- Distância Percorrida]\033[m\n\033[1;34m[4- Tempo do treino]\033[m\n\033[1;35m[5- Localização]\033[m\n\033[1;36m[6- Condições climáticas]\033[m")
                o = int(input("\033[1;37mOque deseja modificar? \033[m"))
                if o == 1:
                    novoNome = input("\033[1;31mDigite o novo nome: \033[m").title()
                    linhas[i] = f"Nome do treino: {novoNome}\n"
                elif o == 2:
                    print("\033[1;32mNova data: \033[m")
                    novaData = f"{int(input("\033[1;32m- Dia: \033[m"))}/{int(input("\033[1;32m- Mês: \033[m"))}/{int(input("\033[1;32m- Ano: \033[m"))}"            
                    linhas[i+1] = f"Data: {novaData}\n"
                elif o == 3:
                    novaDist = f"{int(input('\033[1;33mNova Distância Percorrida (Km): \033[m'))} km"
                    linhas[i+2] = f"Distância Percorrida: {novaDist}\n"
                elif o == 4: 
                    print("\033[1;34mNovo Tempo: \033[m")
                    novoTempo = f"{int(input("\033[1;34m- Hora(s): \033[m"))} hora(s) {int(input("\033[1;34m- Minuto(s): \033[m"))} minuto(s) {int(input("\033[1;34m- Segundo(s): \033[m"))} segundo(s)"
                    linhas[i+3] = f"Tempo: {novoTempo}\n"
                elif o == 5: 
                    novaLoc = f"{input("\033[1;35mNova Localização: \033[m").title()}"
                    linhas[i+4] = f"Localização: {novaLoc}\n"
                elif o == 6:
                    novaCondClim = f"{input("\033[1;36mNovas Condições Climáticas: \033[m").title()}"
                    linhas[i+5] = f"Condições Climáticas: {novaCondClim}\n\n"

        if not treinoEncontrado:
            print("\033[1;31mTreino não encontrado\033[m")
            print()

        with open("registroCorridas.txt", "w", encoding="utf8") as registroCorridas: 
            registroCorridas.writelines(linhas)

    except ValueError:
        print("\033[1;31m#\033[m" * 50)
        print("\033[1;31mEntrada inválida, Digite novamente...\033[m")
        print("\033[1;31m#\033[m" * 50)

def removerTreinos():
    try: 
        listaRestante = []
        treinoEncontrado = False

        nome = input("\033[1;37mDigite o nome do treino que deseja remover: \033[m").title()
        with open("registroCorridas.txt", "r", encoding="utf8") as registroCorridas: 
            linhas = registroCorridas.readlines()

        i = 0
        while i < len(linhas):
            if nome in linhas[i]:
                treinoEncontrado = True   
                i += 6  
            else:
                listaRestante.append(linhas[i]) 
                i += 1 

        with open("registroCorridas.txt", "w", encoding="utf8") as registroCorridas:
            registroCorridas.writelines(listaRestante)

        if treinoEncontrado:
            print("\033[1;32mTreino removido com sucesso!\033[m")
            print()
        else: 
            print("\033[1;31mTreino não encontrado com esse nome.\033[m")
            print()
    except ValueError:
        print("\033[1;31m#\033[m" * 50)
        print("\033[1;31mEntrada inválida, Digite novamente...\033[m")
        print("\033[1;31m#\033[m" * 50)

def AmetasTreinos():
    try: 
        print("\033[1;34m[1- Por treino]\033[m\n\033[1;36m[2- A longo prazo]\033[m")
        opcao = int(input("\033[1;37mEscolha uma opção: \033[m"))
        if opcao == 1:
            kms = float(input("\033[1;34mQuantos quilometros você deseja correr? \033[m"))
            tempo = float(input("\033[1;34mEm quantos MINUTOS deseja alcançar essa meta? \033[m"))
            with open("metasTreinos.txt" , "a", encoding="utf8") as metasTreino:
                metasTreino.write(f"---------------- Por treino -----------------\n")
                metasTreino.write(f"Sua meta é correr {kms} km em {tempo} MINUTOS\n\n")
        elif opcao == 2: 
            kms = float(input("\033[1;36mQuantos quilometros você deseja correr? \033[m"))
            tempo = float(input("\033[1;36mEm quantos DIAS deseja alcançar essa meta? \033[m"))
            with open("metasTreinos.txt", "a" , encoding="utf8") as metasTreino:
                metasTreino.write(f"----------- A longo Prazo ------------\n")
                metasTreino.write(f"Sua meta é correr {kms} em {tempo} DIAS\n\n")
    except ValueError:
        print("\033[1;31m#\033[m" * 50)
        print("\033[1;31mEntrada inválida, Digite novamente...\033[m")
        print("\033[1;31m#\033[m" * 50)
        
def VmetasTreinos():
    try:
        while True: 
            print("\033[1;37mQuais metas deseja ver?\033[m \033[1;34m\n[1- Por treino]\033[m \n\033[1;36m[2- A longo prazo]\033[m")
            opcao = int(input("\033[1;37mEscolha uma opção: \033[m"))
            if opcao == 1:
                busca = "Por treino"
                break
            elif opcao == 2:
                busca = "A longo Prazo"
                break 
            else:
                print("\033[1;31mOpção inválida. Escolha 1 ou 2.\033[m")  

        with open("metasTreinos.txt", "r", encoding="utf8") as metasTreinos:
            metas = metasTreinos.readlines()

            print(f"\033[1;37m\n=== Metas Selecionadas ({busca}) ===\033[m")
            for i, linha in enumerate(metas):
                if busca in linha:
                    print(metas[i+1].strip())
                    print()
    except ValueError:
        print("\033[1;31m#\033[m" * 50)
        print("\033[1;31mEntrada inválida, Digite novamente...\033[m")
        print("\033[1;31m#\033[m" * 50)
        
def sugestTreinos(): 
    try: 
        with open("treinosAleatorios.txt", "r", encoding="utf8") as arquivo:
            treinos = arquivo.readlines()

            numeroAleatorios = random.randint(0, 39)

            print("\n\033[1;34m                 =-=-=-= SUGESTÃO DE TREINO =-=-=-=\033[m")
            print(f"\033[1;37m{treinos[numeroAleatorios]}\033[m" + "\n")

    except ValueError:
        print("\033[1;31m#\033[m" * 50)
        print("\033[1;31mEntrada inválida, Digite novamente...\033[m")
        print("\033[1;31m#\033[m" * 50)

def avaliacaoCorridas():
    try:
        while True: 
            nome = input("\033[1;37mInsira o nome da corrida que você deseja avaliar: \033[m").title()
            avaliacaoTreino = False
            with open("registroCorridas.txt" , "r") as registroCorridas:
                for treino in registroCorridas:
                    if nome in treino:
                        avaliacaoTreino = True
                        break 
            
            if avaliacaoTreino:
                coment = input("\033[1;37mInsira um comentário para essa corrida: \033[m")
                while True: 
                    try:
                        feed = int(input("\033[1;37mInsira uma nota de\033[m \033[1;31m0\033[m a \033[1;32m5\033[m \033[1;37mpara essa corrida: \033[m"))        
                        if 0 < feed > 5:
                            print("\033[1;31mAvaliação Inválida, Digite novamente!!\033[m")
                        else:
                            print("\033[1;32mObrigado pela sua avaliação!\033[m")
                            with open("feedbackCorrida.txt", "a", encoding="utf8") as feedback:
                                feedback.write(f"Corrida: {nome}\nNota: {feed}\n")
                                feedback.write(f"Comentário: {coment}\n{"-" * 45}\n")
                            break 
                    except ValueError:
                        print("\033[1;31mPor favor, insira um número válido!\033[m")
                break 
            else:
                print("\033[1;31mTreino não encontrado\033[m")
                print("\033[1;37mVoltando para o menu principal...\033[m")
                break
    except ValueError:
        print("\033[1;31m#\033[m" * 50)
        print("\033[1;31mEntrada inválida, Digite novamente...\033[m")
        print("\033[1;31m#\033[m" * 50)

while True:
    try: 
        nome = input("\n\033[1;37mDigite o seu nome: \033[m").strip().title()   
        if nome.replace(" ", "").isalpha(): 
            break 
        else:
            print("\033[1;31mNome inválido, Digite novamente...\033[m") 
    except ValueError:
        print("\033[1;31m#\033[m" * 50)
        print("\033[1;31mEntrada inválida, Digite novamente...\033[m")
        print("\033[1;31m#\033[m" * 50)
print("\033[1;33m          GERENCIAMENTO DOS TREINOS DE CORRIDA          \033[m")
print("\033[1;33m-=\033[m" * 30)
print(f"\n\033[1;37mOlá\033[m \033[1;33m{nome},\033[m \n\033[1;37mSeja bem-vindo ao PerifeRun 🏃\033[m\n")

while True:
    try: 
        print("\033[1;32m[1] Adicionar Treinos\033[m \n\033[1;33m[2] Visualizar Treinos\033[m \n\033[1;33m[3] Atualizar Treinos\033[m \n\033[1;31m[4] Excluir Treino \n\033[1;31m[5] Encerrar\033[m")
        o = int(input("\033[1;37mO que deseja fazer?: \033[m"))
        print("\033[1;37m*\033[m" * 50)
        match o:
            case 5:
                break  
            case 1:
                adicionarTreinos()
            case 2:
                visualizarTreinos()
            case 3:
                atualizarTreinos()
            case 4:
                removerTreinos()
            case _:
                print("\033[1;31mOpção inválida, Digite novamente...\033[m")
    except ValueError:
        print("\033[1;31m#\033[m" * 50)
        print("\033[1;31mEntrada inválida, Digite novamente...\033[m")
        print("\033[1;31m#\033[m" * 50)

while True: 
    try: 
        looping = input(f"\033[1;37m{nome}\033[m, \033[1;37mdeseja acessar as funcionalidades extras? \033[m").lower()
        print("\033[1;37m-\033[m" * 50)
        if looping == "não" or looping == "nao" or looping == "n":
            print(f"\033[1;32mEncerrando interação...\033[m")
            print(f"\033[1;32mAté mais, {nome}!!\033[m")
            break 
        elif looping == "sim" or looping == "s":
            while True:
                try:
                    print("\033[1;33m                METAS, SUGESTÕES E FEEDBACKS           \033[m")
                    print("\033[1;33m-=\033[m" * 30)
                    print("\n\033[1;32m[1] Adicionar Meta\033[m \n\033[1;33m[2] Ver Metas\033[m \n\033[1;34m[3] Sugestão de Treino\033[m \033\n[1;35m[4] Feedbacks\033[m \n\033[1;31m[5] Encerrar\033[m")
                    opcao = int(input("\033[1;37mOque deseja fazer? \033[m"))
                    print("\033[1;37m-\033[m" * 35)
                    match opcao:
                        case 1:
                            AmetasTreinos()
                        case 2:
                            VmetasTreinos()
                        case 3:
                            sugestTreinos()
                        case 4:
                            avaliacaoCorridas()
                        case 5:
                            print("\033[1;32mEncerrando interação...\033[m")
                            print(f"\033[1;32mAté mais, {nome}!!\033[m")
                            break 
                        case _:
                            print("\033[1;31mOpção inválida, Digite novamente...\033[m")
                except ValueError:
                    print("\033[1;31m#\033[m" * 50)
                    print("\033[1;31mEntrada inválida, Digite novamente...\033[m")
                    print("\033[1;31m#\033[m" * 50)
            break                 
    except ValueError:
        print("\033[1;31m#\033[m" * 50)
        print("\033[1;31mEntrada inválida, Digite novamente...\033[m")
        print("\033[1;31m#\033[m" * 50)