pacotes = ("ABC123", "XYZ789", "DEF456", "JKL321", "MNO654", "PQR987", "STU741")
rastreio = ("Enviado", "Recebido", "Em Trânsito", "Enviado", "Recebido", "Em Trânsito", "Enviado")
indices = []
pacotes2 = []
# print(len(pacotes))
print("Enviados:", rastreio.count("Enviado"))
print("Recebido:", rastreio.count("Recebido"))
print("Em Trânsito", rastreio.count("Em Trânsito"))

for i in rastreio:
    if i == "Em Trânsito":
        indices.append(pacotes(i))
        # indices = (pacotes[i])
        # pacotes2.append(indices)
        # pacotes2 = pacotes[indices]

print("Pacotes em trânsito:", pacotes2)

rastr = input("Insira o código de rastreamento para ver os status do pacote: ")
if rastr in pacotes:
    print("Posição da primeira ocorrência do número 7:", numero.index(7))