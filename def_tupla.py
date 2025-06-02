numero = (5, 8, 12, 8, 7, 8, 3)
#definindo a tupla precisa estar entre parenteses ()
print("Tupla original:", numero)
#imprimindo para o usuário a tupla original, sem manipulações
print("Tamanho da tupla:", len(numero))
print("Acessando pelo índice",numero[2])
print("Fazendo um slicing do 2 ao 5", numero[2:5])
#o slicing não pega o último item definido no recorte
print("Quantas vezes o número 8 repete:", numero.count(8))
print("Posição da primeira ocorrência do número 7:", numero.index(7))
minimo_tupla = min(numero)
print(minimo_tupla)
maximo_tupla = max(numero)
print(maximo_tupla)
sum_tupla = sum(numero)
print(sum_tupla)
tupla_ordenada = sorted(numero)
print("Os números em ordem utilizando o método sorted", tupla_ordenada)
print("O número 4 está na tupla???:", 4 in numero)
numero2 = (15,20)
tupla_concatenada = numero + numero2
print("A concatenação das tuplas 1 e 2 resulta em uma nova tupla:", tupla_concatenada)
tupla_duplicada = numero*2
print(tupla_duplicada)