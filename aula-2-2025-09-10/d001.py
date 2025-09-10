# Adaptar o código de ex001.py para executar com qualquer quantidade de loops
# Pode utilizar listas
# Pretendo utilizá-las como pilha para os multiplicadores de loop

entrada = input("")

comandos = entrada.split(" ")

custo = 0
multiplicadores = [1] # O primeiro multiplicador (o do nível 0) vai ser sempre 1.

for i in range(len(comandos)):
    if comandos[i] == "IO":
        custo += multiplicadores[-1] * 30
    elif comandos[i] == "MEM":
        custo += multiplicadores[-1] * 10
    elif comandos[i] == "PROCSUM":
        custo += multiplicadores[-1] * 1
    elif comandos[i] == "PROCMULT":
        custo += multiplicadores[-1] * 10
    elif comandos[i] == "LOOP":
        multiplicador = int(comandos[i + 1])
        multiplicadores.append(multiplicador)
    elif comandos[i] == "FIMLOOP":
        multiplicadores.pop() # O método pop, sem parâmetros, remove o último elemento da lista; nesse caso, o último multiplicador da pilha

# Saída:
print(custo)
