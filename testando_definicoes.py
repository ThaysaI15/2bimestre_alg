compras = ["pão", "café", "leite"]
print (compras)
compras.remove(compras[0]) ##pode ser removido pelo nome ou pelo índice
print (compras)
compras.append("açúcar") ##append só pode adicionar um por vez
print (compras)
# compras.sort()
# print (compras)
#é preciso criar uma lista nova para receber os elementos rdenados na lista antiga
compras_ordenada = sorted(compras)
print (compras_ordenada)

for item in compras:
    print("-", item)