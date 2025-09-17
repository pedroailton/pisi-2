# Verificação de divisibilidade por 3

## Método Conversão de Tipos



## Método matemático

### Recursivo

### Loop

n = int(input("Insira n: "))

if n <= 0:
        print("Erro! n deve ser maior que o 0.")
else:
    somaDigitos = 0
    while somaDigitos not in (3, 6, 9) and n >= 10:
        somaDigitos += n % 10
        n = n // 10
    somaDigitos += n

if n in (3, 6, 9):
    print("É divisível por 3!")
elif n < 10:
    print("Não é divisível por 3!")

print(f"Soma dos dígitos: {somaDigitos}")
