import os 
os.system("cls")

import random

def adicionarTreinos():
    try:
        while True: 
            nome = input("Nome do treino: ").strip().title()
            if nome.replace(" ", "").isalnum():
                break
            else:
                print("Nome inválido, digite novamente!")

        while True: 
            print(f"Data do treino: ")
            dia = int(input("- Dia: "))
            mes = int(input("- Mês: "))
            ano = int(input("- Ano: "))

            if 1<= dia <= 31 and 1 <= mes <= 12 and ano > 0:
                break 
            else:
                print("Entrada inválida, digite novamente")
        
        distanciaPercorrida = f"{int(input("Distância Percorrida (Km): "))} km"

        while True:
            print("Tempo de Treino:")
            hora = int(input("- Hora(s): "))
            minutos = int(input("- Minuto(s): "))
            segundos = int(input("- Segundo(s): "))
            if 0 <= minutos <= 59 and 0 <= segundos <= 59:
                break 
            else: 
                print("Entrada inválida, Digite novamente...")

        localizacao = f"{input("Localização: ").title().strip()}"

        while True: 
            condClima = f"{(input("Condições Climáticas: ").title().strip())}"
            if condClima.replace(" ", "").isalpha():
                break
            else:
                print("Entrada inválida, Digite novamente...")
        
        with open("registroCorridas.txt", "a", encoding="utf8") as registroCorridas:
            registroCorridas.write(f"\nNome do treino: {nome}\nData: {dia}/{mes}/{ano}\nDistância Percorrida: {distanciaPercorrida}\nTempo: {hora} hora(s) {minutos} minuto(s) {segundos} segundo(s)\nLocalização: {localizacao}\nCondições Climáticas: {condClima}\n\n")

    except ValueError:
        print("\033[1;31m#\033[m" * 50)
        print("\033[1;31mEntrada inválida, Digite novamente...\033[m")
        print("\033[1;31m#\033[m" * 50)

def visualizarTreinos():
    try: 
        while True: 
            print("Filtrar treinos: \n[1- Distância Percorrida]\n[2- Tempo]\n[3- Voltar]")
            o = int(input("Qual modo deseja filtar o seu treino?: "))
            with open("registroCorridas.txt", "r", encoding="utf8") as registroCorridas:
                linhas = registroCorridas.readlines()

            treinoEncontrado = False
            if o == 1:
                distanciaPercorrida = f"{int(input('Distância Percorrida (Km): '))} km"
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
                    print("Treino não encontrado!")

            elif o == 2:
                print("Tempo de Treino:")
                hora = int(input("- Hora(s): "))
                minutos = int(input("- Minuto(s): "))
                segundos = int(input("- Segundo(s): "))
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
                    print("Treino não encontrado!")
                print()

            elif o == 3:
                print("Voltando para o menu principal...")
                break
            else:
                print("\033[1;31mValor inválido, Digite novamente...[m")
            print()
    except ValueError:
        print("\033[1;31m#\033[m" * 50)
        print("\033[1;31mEntrada inválida, Digite novamente...\033[m")
        print("\033[1;31m#\033[m" * 50)

def atualizarTreinos(): 
    try: 
        treinoEncontrado = False
        nome = input("Qual é o nome do treino que deseja modificar? ").title()
        with open("registroCorridas.txt" , "r", encoding="utf8") as registroCorridas:
            linhas = registroCorridas.readlines()

        for i in range(len(linhas)):
            if nome in linhas[i]:
                treinoEncontrado = True
                print("[1- Nome do treino]\n[2- Data do Treino]\n[3- Distância Percorrida]\n[4- Tempo do treino]\n[5- Localização]\n[6- Condições climáticas]")
                o = int(input("Oque deseja modificar? "))
                if o == 1:
                    novoNome = input("Digite o novo nome: ").title()
                    linhas[i] = f"Nome do treino: {novoNome}\n"
                elif o == 2:
                    print("Nova data: ")
                    novaData = f"{int(input("- Dia: "))}/{int(input("- Mês: "))}/{int(input("- Ano: "))}"            
                    linhas[i+1] = f"Data: {novaData}\n"
                elif o == 3:
                    print("Nova Distância Percorrida: ")
                    novaDist = f"{int(input('Distância Percorrida (Km): '))} km"
                    linhas[i+2] = f"Distância Percorrida: {novaDist}\n"
                elif o == 4: 
                    print("Novo Tempo: ")
                    novoTempo = f"{int(input("- Hora(s): "))} hora(s) {int(input("- Minuto(s): "))} minuto(s) {int(input("- Segundo(s): "))} segundo(s)"
                    linhas[i+3] = f"Tempo: {novoTempo}\n"
                elif o == 5: 
                    print("Nova Localização: ")
                    novaLoc = f"{input("Localização: ").title()}"
                    linhas[i+4] = f"Localização: {novaLoc}\n"
                elif o == 6:
                    print("Nova Condição Climática: ").title()
                    novaCondClim = f"{input("Condições Climáticas: ")}"
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

        nome = input("Digite o nome do treino que deseja remover: ").title()
        with open("registroCorridas.txt", "r", encoding="utf8") as registroCorridas: 
            linhas = registroCorridas.readlines()

        i = 0
        while i < len(linhas):
            if nome in linhas[i]:
                treinoEncontrado = True  # apneas para dar o feedback para usuário 
                i += 6  # vai ignorar as próximas 6 linhas pra pular o bloco do treino todo
            else:
                listaRestante.append(linhas[i])  # aqui vai adicionar a uma lista o restante da lista que não entrou no parametro de cima
                i += 1  # é o incremento para poder acabar o looping

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
        print("        ADICIONAR METAS         ")
        print("-=" * 15)
        print("[1- Por treino]\n[2- A longo prazo]")
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            kms = float(input("Quantos kilometros você deseja correr? "))
            tempo = float(input("Em quantos MINUTOS deseja alcançar essa meta? "))
            with open("metasTreinos.txt" , "a", encoding="utf8") as metasTreino:
                metasTreino.write(f"---------------- Por treino -----------------\n")
                metasTreino.write(f"Sua meta é correr {kms} km em {tempo} MINUTOS\n\n")
        elif opcao == 2: 
            kms = float(input("Quantos kilometros você deseja correr? "))
            tempo = float(input("Em quantos DIAS deseja alcançar essa meta? "))
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
            print("Quais metas deseja ver? \n[1- Por treino]\n[2- A longo prazo]\n[3- Voltar]")
            opcao = int(input("Escolha uma opção: "))
            if opcao == 1:
                busca = "Por treino"
                break
            elif opcao == 2:
                busca = "A longo Prazo"
                break 
            else:
                print("Opção inválida. Escolha 1 ou 2.")  

        with open("metasTreinos.txt", "r", encoding="utf8") as metasTreinos:
            metas = metasTreinos.readlines()

            print(f"\n=== Metas Selecionadas ({busca}) ===")
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
            nome = input("Insira o nome da corrida que você deseja avaliar: ").title()
            avaliacaoTreino = False
            with open("registroCorridas.txt" , "r") as registroCorridas:
                for treino in registroCorridas:
                    if nome in treino:
                        avaliacaoTreino = True
                        break 
            
            if avaliacaoTreino: 
                break 
            else: 
                print("\033[1;31mTreino não encontrado, Digite novamente!!!\033[m")
        
        coment = input("Insira um comentário para essa corrida: ")
        while True:
            feed = int(input("Insira uma nota de \033[1;31m0\033[m a \033[1;32m5\033[m para essa corrida: "))        
            if 0 < feed > 5:
                print("Avaliação Inválida, Digite novamente!!")
            else:
                break

        with open("feedbackCorrida.txt", "a", encoding="utf8") as feedback:
            feedback.write(f"Corrida: {nome}\nNota: {feed}\n")
            feedback.write(f"Comentário: {coment}\n{"-" * 45}\n")

    except ValueError:
        print("\033[1;31m#\033[m" * 50)
        print("\033[1;31mEntrada inválida, Digite novamente...\033[m")
        print("\033[1;31m#\033[m" * 50)

print("\033[1;33m          GERENCIAMENTO DOS TREINOS DE CORRIDA          \033[m")
print("\033[1;33m-=\033[m" * 30)
while True:
    try: 
        nome = input("\nDigite o seu nome: ").strip().title() #strip - retira os espaços vazios da frente e de tras   
        if nome.replace(" ", "").isalpha(): # eu vou retirar os espaços vazios para conferir se tem apenas letras no input
            break # caso tenha apenas letras no input, iremos quebrar o looping 
        else:
            print("\033[1;31mNome inválido, Digite novamente...\033[m") # caso não consiga seguir as condições acima, printará esse comando e entrará no looping novamente
    except ValueError:
        print("\033[1;31m#\033[m" * 50)
        print("\033[1;31mEntrada inválida, Digite novamente...\033[m")
        print("\033[1;31m#\033[m" * 50)
print(f"\n\033[1;35m-=-=-=-=-=-=-=-=-= Bem vindo ao PERIFERUN, \033[1;32m{nome}\033[m \033[1;35m-=-=-=-=-=-=-=-=-=\033[m")

while True:
    try: 
        print("\033[1;32m[1] Adicionar Treinos\033[m \n\033[1;33m[2] Visualizar Treinos\033[m \n\033[1;33m[3] Atualizar Treinos\033[m \n\033[1;31m[4] Excluir Treino \n\033[1;31m[5] Encerrar\033[m")
        o = int(input("O que deseja fazer?: "))
        print("*" * 50)
        if o == 5:
            break 

        if o == 1:
            adicionarTreinos()
        elif o == 2: 
            visualizarTreinos()
        elif o == 3:
            atualizarTreinos()
        elif o == 4: 
            removerTreinos()
        elif o > 5:
            print("Opção inválida, Digite novamente...")
    except ValueError:
        print("\033[1;31m#\033[m" * 50)
        print("\033[1;31mEntrada inválida, Digite novamente...\033[m")
        print("\033[1;31m#\033[m" * 50)

while True: 
    try: 
        looping = input(f"{nome}, deseja acessar as funcionalidades extras? ").lower()
        print("-" * 50)
        if looping == "não" or looping == "nao" or looping == "n":
            print(f"Encerrando interação...")
            print(f"Até mais, {nome}!!")
            break 
        elif looping == "sim" or looping == "s":
            while True:
                try:
                    print("             METAS, SUGESTÕES E FEEDBACKS           ")
                    print("-=" * 25)
                    print("Oque deseja fazer? \n\033[1;32m[1] Adicionar Meta\033[m \n\033[1;33m[2] Ver Metas\033[m \n\033[1;34m[3] Sugestão de Treino\033[m \033\n[1;35m[4] Feedbacks\033[m \n\033[1;31m[5] Encerrar\033[m")
                    opcao = int(input("Oque deseja fazer? "))
                    print("-" * 35)
                    if opcao == 1:
                        AmetasTreinos()
                    elif opcao == 2:
                        VmetasTreinos()
                    elif opcao == 3:
                        sugestTreinos()
                    elif opcao == 4:
                        avaliacaoCorridas()
                    elif opcao == 5:
                        print("Encerrando interação...")
                        print(f"Até mais, {nome}!!")
                        break 
                    else:
                        print("Opção inválida, Digite novamente...")
                except ValueError:
                    print("#" * 40)
                    print("Entrada inválida, Digite novamente...")
                    print("#" * 40)
            break                 
    except ValueError:
        print("\033[1;31m#\033[m" * 50)
        print("\033[1;31mEntrada inválida, Digite novamente...\033[m")
        print("\033[1;31m#\033[m" * 50)