def fat(n):
    if n < 0:
        return None
    elif n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * fat(n - 1)
    
n = int(input("Insira o número para a operação do fatorial: "))

print(f"Resultado: {fat(n)}")