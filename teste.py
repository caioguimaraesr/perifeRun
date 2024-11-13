import random 

with open("treinosAleatorios.txt", "r", encoding="utf8") as arquivo: 
    linhas = arquivo.readlines()

    numeroAleatorio = random.randint(0, 19)

    print(linhas[numeroAleatorio])
    
    linhas.pop(numeroAleatorio)