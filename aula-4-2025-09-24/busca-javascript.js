function buscaLinear(arr, alvo) {
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === alvo) {
            return i; // Retorna o índice do elemento encontrado
        } 
}

buscaLinear([10, 20, 30, 40, 50], 30); // Retorna 2   }
    return -1; // Retorna -1 se o elemento não for encontrado
}
// Exemplo de uso:
console.log(buscaLinear([10, 20, 30, 40, 50], 30)); // Retorna 2
console.log(buscaLinear([10, 20, 30, 40, 50], 60)); // Retorna -1
