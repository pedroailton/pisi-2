def buscaLinear(lista, elemento):
    """
    Realiza uma busca linear em uma lista.
    Retorna o índice do elemento se encontrado, ou -1 se não estiver na lista.
    A ordem é O(n).
    Não é necessária uma lista ordenada
    """
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1

def buscaBinaria(lista, elemento):
    """
    Realiza uma busca binária em uma lista ordenada.
    Retorna o índice do elemento se encontrado, ou -1 se não estiver na lista.
    A ordem é O(log n).
    Requer uma lista ordenada.
    """
    esquerda, direita = 0, len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == elemento:
            return meio
        elif lista[meio] < elemento:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1

def ordenacaoPorInsercao(lista):
    """
    Ordena uma lista usando o algoritmo de ordenação por inserção.
    """
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and chave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave
    return lista

# Exemplo de uso
if __name__ == "__main__":
    lista = [10, 23, 45, 70, 11, 15]

    # Ordenação por Inserção
    lista_ordenada = ordenacaoPorInsercao(lista.copy())

    # Busca Linear
    elemento = 70
    indice = buscaLinear(lista, elemento)
    if indice != -1:
        print(f"Elemento {elemento} encontrado no índice {indice}.")
    else:
        print(f"Elemento {elemento} não encontrado na lista.")