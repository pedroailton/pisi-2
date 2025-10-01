pilha = []

entrada = input('Digite uma palvra ou frase para verificar se é palíndromo: ').strip()

for letra in entrada:
    pilha.append(letra)

for letra in entrada:
    if letra != pilha.pop(): # Comparação de um índice com uma pilha que vai decrescendo a cada iteração
        print("Não é um palíndromo!")
        break
else:
        print("É um palíndromo!")