# Sequência de Fibonacci
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

n = int(input("digite o valor de n: "))

if n <= 0:
    resultado = None
elif n == 1:
    resultado = 0
elif n == 2:
    resultado = 1
else:
    penultimo = 0
    ultimo = 1
    novo = ultimo + penultimo # Considera apenas o ultimo, para não gastar processamento com uma operação de soma com um valor que vai ser sempre 0.
    for i in range(3, n + 1):
        novo = penultimo + ultimo
        penultimo = ultimo
        ultimo = novo
    resultado = novo

print(resultado)
