pacotes = ("ABC123", "XYZ789", "DEF456", "JKL321", "MNO654", "PQR987", "STU741")
rastreio = ("Enviado", "Recebido", "Em Trânsito", "Enviado", "Recebido", "Em Trânsito", "Enviado")
indices = []
pacotes2 = [pacotes]
# print(len(pacotes))
print("Enviados:", rastreio.count("Enviado"))
print("Recebido:", rastreio.count("Recebido"))
print("Em Trânsito", rastreio.count("Em Trânsito"))

for i in rastreio:
    if rastreio[i] == "Em Trânsito":
        indices.append(pacotes2[i])
print ("Pacotes em Trânsito: ", indices)

rastreamento = input("insira o código do rastreamento: ")
for i in pacotes:
    if rastreamento == pacotes[i]:
        indice = i
        print ("O status do pacote é: ", rastreio[indice])
    if rastreamento != pacotes[i]:
        print ("Pacote não está cadastrado")
