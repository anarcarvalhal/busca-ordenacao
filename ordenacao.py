def _median_of_three_and_swap(lista, inicio, fim):
    """
    Encontra a mediana entre o primeiro, do meio e último elementos, posicionando-a no final
    da lista para ser usada como pivô. Essa técnica busca evitar o pior caso do Quicksort.
    Retorna o número de comparações realizadas.
    """

    meio = (inicio + fim) // 2
    comparacoes = 0

    # Ordena os três elementos (inicio, meio, fim) para encontrar a mediana
    comparacoes += 1
    if lista[inicio] > lista[meio]:
        lista[inicio], lista[meio] = lista[meio], lista[inicio]
    comparacoes += 1
    if lista[inicio] > lista[fim]:
        lista[inicio], lista[fim] = lista[fim], lista[inicio]
    comparacoes += 1
    if lista[meio] > lista[fim]:
        lista[meio], lista[fim] = lista[fim], lista[meio]

    # Agora, lista[meio] é a mediana. Coloca ela no fim para ser o pivô.
    lista[meio], lista[fim] = lista[fim], lista[meio]

    return comparacoes

def _partition(lista, inicio, fim):
    """
    Particiona a lista usando o elemento pivô (último elemento) 
    e retorna uma tupla com o índice do pivô e o número de comparações.
    """
    
    comparacoes = 0
    pivo = lista[fim]    
    i = inicio - 1       

    # Rearranja os elementos: menores que o pivô à esquerda, maiores à direita.
    for j in range(inicio, fim):
        comparacoes += 1
    
        if lista[j] <= pivo:
            i += 1
            lista[i], lista[j] = lista[j], lista[i] 

    # Posiciona corretamente o pivô.
    lista[i + 1], lista[fim] = lista[fim], lista[i + 1]
    return i + 1, comparacoes

def _quick_sort_in_place(lista, inicio, fim):
 """Ordena lista in-place com QuickSort e retorna o número de comparações."""
    
    comparacoes = 0
    if inicio < fim:

        comp_mediana = _median_of_three_and_swap(lista, inicio, fim)
        comparacoes += comp_mediana

        # Particiona a lista e obtém o índice do pivô e as comparações da partição
        pivo_idx, comp_particao = _partition(lista, inicio, fim)
        comparacoes += comp_particao
        
        # Ordena recursivamente as duas sub-listas
        comp_esquerda = _quick_sort_in_place(lista, inicio, pivo_idx - 1)
        comp_direita = _quick_sort_in_place(lista, pivo_idx + 1, fim)
        
        comparacoes += comp_esquerda + comp_direita
    return comparacoes

def quick_sort(lista):
    """Interface principal para o QuickSort. Retorna a lista ordenada e o número de comparações."""
    lista_ordenada = list(lista) 
    comparacoes = _quick_sort_in_place(lista_ordenada, 0, len(lista_ordenada) - 1)

    return lista_ordenada, comparacoes
