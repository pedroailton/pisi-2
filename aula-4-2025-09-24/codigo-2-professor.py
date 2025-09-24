def buscaBinaria(lista, alvo):
    inicio = 0
    fim = len(lista) - 1 ## Índice do último elemento (sem considerar o elemento 0 como quantidade)

    while inicio <= fim:
        meio = (inicio + fim) // 2 ## Arrendonda para baixo
        if lista[meio] == alvo: ## Caso base da recursão
            return meio
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1  ## Elemento não encontrado

# Programa Principal
from random import randint, shuffle

