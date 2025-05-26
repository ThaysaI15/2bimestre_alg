sair = 1
compras = []
while sair == 1:
    print("Sua lista atual:", compras)
    op = int(input("\nDeseja incluir um item ao seu carrinho de compras?\n \n1 - Sim\n2 - Não\n3 - Sair\n\nR= "))
    if op == 1:
        item = input("\nInsira o item: ")
        compras.append(item.lower())
    if op == 2:
        op2 = int(input("\nDeseja remover algum item da lista?\n \n1 - Sim\n2 - Não\n\nR= "))
        print("\nSua lista atual:", compras)
        if op2 == 1:
            item = input("\nQual item deseja remover?\n\nR= ")
            compras.remove(item.lower())
        if op2 != 2 and op2 != 1:
            print("\nValor inválido digitado")
    if op == 3:
        sair = 0 
    if op < 1 and op > 3:
        print("\nOperação inválida")
if sair == 0:
    print("\nAplicativo encerrado.")