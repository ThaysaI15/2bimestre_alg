pacotes = ("ABC123", "XYZ789", "DEF456", "JKL321", "MNO654", "PQR987", "STU741")
rastreio = ("Enviado", "Recebido", "Em Trânsito", "Enviado", "Recebido", "Em Trânsito", "Enviado")
indices = []
pacotes2 = [pacotes]
# print(len(pacotes))
print("Enviados:", rastreio.count("Enviado"))
print("Recebido:", rastreio.count("Recebido"))
print("Em Trânsito", rastreio.count("Em Trânsito"))

for i in rastreio:
    if i == "Em Trânsito":
        indices.append(pacotes2[i])

rastreamento = input("insira o código do rastreamento: ")
for i in pacotes:
    if rastreamento == pacotes[i]:
        indice = i
        print ("O status do pacote é: ", rastreio[indice])


# print("Pacotes em trânsito:", pacotes2)

# rastr = input("Insira o código de rastreamento para ver os status do pacote: ")
# if rastr in pacotes:
#     print("Posição da primeira ocorrência do número 7:", numero.index(7))