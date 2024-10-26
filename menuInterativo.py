import os 
os.system("cls")

def adicionarTreinos():
    nome = input("Nome do treino: ")
    print(f"Data do treino: ")
    data = f"{int(input("- Dia: "))}/{int(input("- Mês: "))}/{int(input("- Ano: "))}"
    distanciaPercorrida = f"{int(input("Distância Percorrida (Km): "))} km"
    print("Tempo de Treino:")
    tempo = f"{int(input("- Hora(s): "))} hora(s) {int(input("- Minuto(s): "))} minuto(s) e {int(input("- Segundo(s): "))} segundo(s)"
    localizacao = f"{input("Localização: ")}"
    condClima = f"{int(input("Condições Climáticas: "))}"
    
    with open("registroCorridas.txt", "a") as registroCorridas:
        registroCorridas.write(f"\nNome do treino: {nome}\nData: {data}\nDistância Percorrida: {distanciaPercorrida}\nTempo: {tempo}\nLocalização: {localizacao}\nCondições Climáticas: {condClima}°\n\n")

def visualizarTreinos():
    print("Filtrar treinos: \n[1- Distância Percorrida]\n[2- Tempo]")
    o = int(input("Qual modo deseja filtar o seu treino?: "))
    with open("registroCorridas.txt", "r") as registroCorridas:
        linhas = registroCorridas.readlines()

    if o == 1:
        distanciaPercorrida = f"{int(input('Distância Percorrida (Km): '))} km"
        print()
        for i, linha in enumerate(linhas):
            if distanciaPercorrida in linha:
                print("-" * 20)
                print(linhas[i-2].strip()) # nome do treino 
                print(linhas[i-1].strip())  # data
                print(linha.strip()) # distância percorrida
                print(linhas[i+1].strip()) # tempo
                print(linhas[i+2].strip()) # localização 
                print(linhas[i+3].strip()) # condições climáticas
                print("-" * 20)
    elif o == 2:
        print("Tempo de Treino:")
        tempo = f"{int(input("- Hora(s): "))} hora(s) {int(input("- Minuto(s): "))} minuto(s) e {int(input("- Segundo(s): "))} segundo(s)"
        print()
        for i, linha in enumerate(linhas):
            if tempo in linha:
                print(linhas[i-3].strip()) # nome do treino
                print(linhas[i-2].strip())  # data
                print(linhas[i-1].strip()) # distância percorrida
                print(linha.strip()) # tempo
                print(linhas[i+1].strip()) # localização 
                print(linhas[i+2].strip()) # condições climáticas
                print("-" * 20)
        print()


def atualizarTreinos():
    nome = input("Qual é o nome da lista que deseja modificar? ")
    with open("registroCorridas.txt" , "r") as registroCorridas:
        linhas = registroCorridas.readlines()

    for i in range(len(linhas)):
        if nome in linhas[i]:
            print("[1- Nome do treino]\n[2-Data do Treino]\n[3- Distância Percorrida]\n[4- Tempo do treino]\n[5- Localização]\n[6- Condições climáticas]")
            o = int(input("Oque deseja modificar? "))
            if o == 1:
                novoNome = input("Digite o novo nome: ")
                linhas[i] = f"Nome do treino: {novoNome}\n"
            elif o == 2:
                print("Nova data: ")
                novaData = f"{int(input("- Dia: "))}/{int(input("- Mês: "))}/{int(input("- Ano: "))}\n"            
                linhas[i+1] = f"Data: {novaData}"
            elif o == 3:
                print("Nova Distância Percorrida: ")
                novaDist = f"{int(input('Distância Percorrida (Km): '))} km"
                linhas[i+2] = f"Distância Percorrida: {novaDist}"
            elif o == 4: 
                print("Novo Tempo: ")
                novoTempo = f"{int(input("- Hora(s): "))} hora(s) {int(input("- Minuto(s): "))} minuto(s) e {int(input("- Segundo(s): "))} segundo(s)"
                linhas[i+3] = f"Tempo: {novoTempo}"
            elif o == 5: 
                print("Nova Localização: ")
                novaLoc = f"{input("Localização: ")}"
                linhas[i+4] = f" Localização: {novaLoc}"
            elif o == 6:
                print("Nova Condição Climática: ")
                novaCondClim = f"{int(input("Condições Climáticas: "))}"
                linhas[i+5] = f"Condições Climáticas: {novaCondClim}°"

    with open("registroCorridas.txt", "w") as registroCorridas: 
        registroCorridas.writelines(linhas)


def removerTreinos():
    listaRestante = []
    treinoEncontrado = False
    i = 0 

    nome = input("Digite o nome do treino que deseja remover: ")
    with open("registroCorridas.txt" , "r") as registroCorridas: 
        linhas = registroCorridas.readlines()
    
    for i in range(len(linhas)):
        if nome in linhas[i]:
            treinoEncontrado = True # apenas para dar o feedback para o usuário 
            i += 5 #vai ignorar o nome que eu coloquei e as próximas 5 linhas que são todos os registros da corrida
        else:
            listaRestante.append(linhas[i]) #aqui vai adicionar a uma lista o restante da lista que nao entrou no paramentro acima 

    with open("registroCorridas.txt", "w") as registroCorridas: # "w" vai substituir todo o conteudo do arquivo txt 
        registroCorridas.writelines(listaRestante) # vai reescrever linha por linha (writelines) todos os arquivos que entraram na lista(listaRestante)

    if treinoEncontrado: # feedback para o usuário 
        print("Treino removido com sucesso!") 
    else: 
        print("Treino não encontrado com esse nome")

# def metasTreinos():

# def sugestTreinos():

# def funcExtra():        

print("GERENCIAMENTO DE TREINOS DE CORRIDA")
print("*" * 40)
while True: 
    print("[1- Adicionar Treinos]\n[2- Visualizar Treinos]\n[3- Atualizar Treinos]\n[4- Excluir Treinos]\n[5- Encerrar]")
    o = int(input("Oque deseja fazer?: "))
    print("*" * 40)
    
    if o == 5:
        print(f"Encerrando Menu de Corridas...")
        break 

    if o == 1:
        adicionarTreinos()
    elif o == 2: 
        visualizarTreinos()
    elif o == 3:
        atualizarTreinos()
    elif o == 4: 
        removerTreinos()
