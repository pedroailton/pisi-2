entrada = input("")

comandos = entrada.split(" ")

custo = 0
nivel = 0
erro = 0

for i in range(len(comandos)):
    if nivel == 2:
        if comandos[i] == "IO":
            custo += mult2 * 30
        elif comandos[i] == "MEM":
            custo += mult2 * 10
        elif comandos[i] == "PROCSUM":
            custo += mult2 * 1
        elif comandos[i] == "PROCMULT":
            custo += mult2 * 10
        elif comandos[i] == "LOOP":
            print("Nosso programa só consegue contar o tempo de um programa com 2 aninhamentos. Você ultrapassou esse número.  Tente novamente.")
            erro = 1
        elif comandos[i] == "FIMLOOP":
            nivel -= 1

    elif nivel == 1:

        if comandos[i] == "IO":
            custo += mult1 * 30
        elif comandos[i] == "MEM":
            custo += mult1 * 10
        elif comandos[i] == "PROCSUM":
            custo += mult1 * 1
        elif comandos[i] == "PROCMULT":
            custo += mult1 * 10
        elif comandos[i] == "LOOP":
            mult2 = int(comandos[i + 1])
            nivel += 1
        elif comandos[i] == "FIMLOOP":
            nivel -= 1
    else:
        if comandos[i] == "IO":
            custo += 30
        elif comandos[i] == "MEM":
            custo += 10
        elif comandos[i] == "PROCSUM":
            custo += 1
        elif comandos[i] == "PROCMULT":
            custo += 10
        elif comandos[i] == "LOOP":
            mult1 = int(comandos[i + 1])
            nivel += 1

# Saída:
if erro != 1:
    print(custo)
