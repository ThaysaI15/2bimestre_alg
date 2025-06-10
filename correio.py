pacotes = (("ABC123", "Enviado"),("XYZ789", "Recebido"),("DEF456", "Em Trânsito"),("JKL321", "Enviado"),("MNO654", "Recebido"),("PQR987", "Em Trânsito"),("STU741", "Enviado"))

cont = {"Enviado": 0, "Recebido": 0, "Em Trânsito": 0}

for codigo, status in pacotes:
    cont[status] = cont[status]+1

print("Contagem de pacotes por status: ")
print("Enviado:", cont["Enviado"])
print("Recebido:", cont["Recebido"])
print("Em Trânsito:", cont["Em Trânsito"])

transito = (cont["Em Trânsito"])

print("\nPacotes em trânsito:", transito,"\n")

def pesq(rastreamento, pacotes):
    if codigo.upper() == rastreamento.upper():
            return f"O pacote '{rastreamento}' está com status: {status}"
    return "Pacote não cadastrado."

codigo = input("Digite o código de rastreamento do pacote: ").strip()
print(pesq(codigo, pacotes))

pacotes_ordenados = (sorted(pacotes))

print("\nPacotes Ordenados:\n")
for pacotes in pacotes_ordenados:
    print(pacotes)