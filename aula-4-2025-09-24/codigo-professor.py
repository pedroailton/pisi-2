# Busca Linear

from random import randint

lista = [randint(1, 1000000) for i in range(1000000)]
## Utiliza o resto da divisão pela faixa de números que você pedius para separar os números que ela já sorteia internamente, de aproximadamente -2bilhões a +2bilhões

print("Tamanho da lista:", len(lista))

print("Primeiros 20 elementos: ", lista[0:20])

continuar = True

while continuar:
    elemento = int(input("Elemento a buscar: "))

    print("Buscando...")

    for i in range(len(lista)):
        if lista[i] == elemento:
            print(f"Elemento {elemento} encontrado no índice: ", i)
            break
    else:
        print(f"Elemento {elemento} não encontrado")

    ## Procurar novamente?
    resp = str(input("Continuar? (s/n) "))
    if resp.lower() != 's':
        continuar = False

print("Fim do programa")