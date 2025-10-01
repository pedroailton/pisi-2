entrada = input("").split()

custo = 0
nivel = 0
erro = 0

mult1 = mult2 = 1
temp1 = temp2 = 0  # acumuladores temporários

for i in range(len(entrada)):
    cmd = entrada[i]

    if nivel == 2:  # dentro de loop interno
        if cmd == "IO":
            temp2 += 30
        elif cmd == "MEM":
            temp2 += 10
        elif cmd == "PROCSUM":
            temp2 += 1
        elif cmd == "PROCMULT":
            temp2 += 10
        elif cmd == "LOOP":
            print("Erro: mais de 2 níveis de loop.")
            erro = 1
        elif cmd == "FIMLOOP":
            temp1 += temp2 * mult2
            temp2 = 0
            nivel -= 1

    elif nivel == 1:  # dentro de loop externo
        if cmd == "IO":
            temp1 += 30
        elif cmd == "MEM":
            temp1 += 10
        elif cmd == "PROCSUM":
            temp1 += 1
        elif cmd == "PROCMULT":
            temp1 += 10
        elif cmd == "LOOP":
            mult2 = int(entrada[i + 1])
            temp2 = 0
            nivel += 1
        elif cmd == "FIMLOOP":
            custo += temp1 * mult1
            temp1 = 0
            nivel -= 1

    else:  # fora de loop
        if cmd == "IO":
            custo += 30
        elif cmd == "MEM":
            custo += 10
        elif cmd == "PROCSUM":
            custo += 1
        elif cmd == "PROCMULT":
            custo += 10
        elif cmd == "LOOP":
            mult1 = int(entrada[i + 1])
            temp1 = 0
            nivel += 1

# Saída
if erro != 1:
    print(custo)
