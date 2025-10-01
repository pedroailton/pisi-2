entrada = input("").strip().upper()

entrada = entrada.split(" ")

comandos = {
    'IO': 30,
    'MEM': 10,
    'PROCSUM': 1,
    'PROCMULT': 10,
}

pilha = []

if entrada[0] != "INICIO" or entrada[-1] != "FIM":
    print('ERRO')
else:
    entrada = entrada[1: -1]

    pos = 0
    while pos < len(entrada): # Varrendo a lista pelo índice pos
        if entrada[pos] == 'LOOP':
            pos += 1
            multiplicador = entrada[pos]
            pilha.append(int(multiplicador)) # O multiplicador é adicionado primeiro na pilha, visando a retirada posterior dos elementos da pilha, lendo primeiro o loop e depois o multiplicador
            pilha.append('LOOP')
        elif entrada[pos] == 'FIMLOOP':
            soma = 0
            elemento = pilha.pop()
            while elemento != 'LOOP':
                soma += elemento
                elemento = pilha.pop() # Retirada do próximo elemento da pilha
            mulltiplicador = pilha.pop()
            custoTotal = soma * multiplicador
            pilha.append(custoTotal)
        elif entrada[pos] in comandos: # Se o valor for um dos comandos (for igual a alguma das chaves)
            valor = comandos[entrada[pos]]
            pilha.append(valor)
        else:
            print('Erro! Entrada inválida', entrada[pos])
            exit()
        pos += 1 # Incrementa o índice

        # Somando a pilha:
        total = 0
        while len(pilha) > 0:
            elem = pilha.pop()
            total += elem
        print(total)