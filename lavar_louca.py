import time

#variaveis blobais
ligado = False
tempo = 0
temperatura = 0

def ligar(novo_tempo, nova_temperatura):
    global ligado, tempo, temperatura
    if not ligado:
        ligado = True
        tempo = novo_tempo
        temperatura = nova_temperatura
        print (f"Máquina ligada por {tempo} segundos na temperatura {temperatura}°C")
        iniciar_cronometro(tempo)
        desligar() #desligar automaticamente
    else:
        print("A máquina já está ligada")


def desligar():
    global ligado
    if ligado:
        ligado = False
        print("A máquina está desligada. Louça pronta para recolher")
    else:
        print("A máquina já está desligada")

def status():
    if ligado:
        print(f"Tempo: {tempo} segundos \n temperatura: {temperatura}°C")
    else:
        print(f"desligado")

def iniciar_cronometro(segundos):
    while segundos > 0:
        print(f"Tempo restante: {segundos} segundos", end="\r")
        time.sleep(1)
        segundos -= 1
    print ("\n Tempo esgotado")

#pré-definições do micro-ondas
def vidro():
    ligar(120, 100)
def plastico():
    ligar(60, 21)
def metal():
    ligar(120, 30)

modo = int(0)
while modo < 1 or modo > 3:
    modo = int(input("\nInsira o modo que deseja rodar: \n\n 1 - Vidro \n 2 - Plástico \n 3 - Metal \n\n Resposta: "))
    if modo == 1:
        vidro()
    if modo == 2:
        plastico()
    if modo == 3:
        metal()