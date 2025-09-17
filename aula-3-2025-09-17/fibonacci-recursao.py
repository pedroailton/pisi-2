from functools import lru_cache

@lru_cache # Utiliza a capacidade máxima de cache

# @lru_cache(maxsize=3) # Python precisa apenas de 3 de tamanho na memória cache de maneira útil

# Não use para funções com sorteio para não utilizar o sorteio feito na execução anterior da função

# Sequência de Fibonacci
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

def fib(n):
    if n <= 0:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
num = int(input("Insira a posição desejada na sequência fibonacci: "))
print(fib(num))