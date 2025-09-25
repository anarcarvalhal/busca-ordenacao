def busca_linear(lista, alvo):
  
    # Variável para estimar as comparações realizadas durante a busca. 
    comparacoes = 0 
    for i in range(len(lista)):
        comparacoes += 1
        if lista[i] == alvo:
            return i, comparacoes
        
    return -1, comparacoes

def busca_binaria(lista_ordenada, alvo):
    
    comparacoes = 0
    inicio = 0 
    fim = len(lista_ordenada) - 1 
    
    # Enquanto o espaço de busca é válido, encontra o índice do meio para comparar.
    while inicio <= fim:
        meio = (inicio + fim) // 2
        comparacoes += 1
        if lista_ordenada[meio] == alvo:
            return meio, comparacoes
        elif lista_ordenada[meio] < alvo:
            inicio = meio + 1  # Se o meio é menor que o alvo, exclui a primeira metade da lista.
        else:
            fim = meio - 1  # Se o meio é maior que o alvo, exclui a segunda metade da lista.

    return -1, comparacoes
