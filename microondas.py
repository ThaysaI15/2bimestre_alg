import time

#variaveis blobais
ligado = False
tempo = 0
potencia = 0

def ligar(novo_tempo, nova_potencia):
    global ligado, tempo, potencia
    if not ligado:
        ligado = True
        tempo = novo_tempo
        potencia = nova_potencia
        print (f"Micro-ondas ligado por {tempo} segundos na potência {potencia}")
        iniciar_cronometro(tempo)
        desligar() #desligar automaticamente
    else:
        print("O micro-ondas já está ligado")

def desligar():
    global ligado
    if ligado:
        ligado = False
        print("Micro-ondas está desligado")
    else:
        print("Micro-ondas já está desligado")

def status():
    if ligado:
        print(f"Tempo: {tempo} segundos \n potência: {potencia}")
    else:
        print(f"desligado")

def iniciar_cronometro(segundos):
    while segundos > 0:
        print(f"Tempo restante: {segundos} segundos", end="\r")
        time.sleep(1)
        segundos -= 1
    print ("\n Tempo esgotado")

#pré-definições do micro-ondas
def pipoca():
    ligar(30, 100)

#rodar a função
pipoca()