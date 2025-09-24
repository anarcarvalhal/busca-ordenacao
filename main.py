"""
Módulo principal para análise de algoritmos de busca e ordenação.

Fornece funções para carregar dados, medir performance e comparar
algoritmos em diferentes cenários de teste.
"""

import random
import time
import sys
import os

from ordenacao import quick_sort
from busca import busca_linear, busca_binaria

# ===============================================================================
#                             PREPARAÇÃO DOS DADOS
# ===============================================================================

def carregar_palavras_de_arquivo(caminho_do_arquivo):
    """
    Lê um arquivo de texto e retorna uma lista de palavras em minúsculas, sem linhas vazias.
    Encerra o programa se o arquivo não for encontrado.
    """
    try:
        with open(caminho_do_arquivo, 'r', encoding='utf-8') as arquivo:
            return [linha.strip().lower() for linha in arquivo if linha.strip()]
        
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_do_arquivo}' não foi encontrado.")
        sys.exit(1)


def gerar_lista_aleatoria(fonte_de_palavras, tamanho): 
    """Gera uma lista aleatória com repetições a partir de uma fonte."""

    if not fonte_de_palavras:    
        raise ValueError("A fonte de palavras não pode estar vazia")
    return random.choices(fonte_de_palavras, k=tamanho)   

def construir_caminho_arquivo(nome_arquivo):
    """Retorna o caminho absoluto e validado para um arquivo."""

    try:
        diretorio_script = os.path.dirname(os.path.abspath(__file__))
        caminho = os.path.join(diretorio_script, nome_arquivo)
        
        if not os.path.exists(caminho): # Verifica se o arquivo realmente existe
            raise FileNotFoundError(f"O arquivo '{caminho}' não foi encontrado.")
        return caminho
    
    except NameError:  # Quando o ambiente não define __file__:
        if not os.path.exists(nome_arquivo):
            raise FileNotFoundError(f"O arquivo '{nome_arquivo}' não foi encontrado.")
        return nome_arquivo
    

def preparar_lista(fonte_de_palavras, tamanho):
    """Gera a lista de teste e ajusta o limite de recursão."""

    if not fonte_de_palavras:
        raise ValueError("A fonte de palavras não pode estar vazia")
    
    sys.setrecursionlimit(tamanho + 200)  
    random.seed(3)  # Para resultados reproduzíveis

    lista = random.choices(fonte_de_palavras, k=tamanho)  
    return lista
    
# ===============================================================================
#                        MEDIÇÃO E EXIBIÇÃO DO DESEMPENHO
# ===============================================================================

def medir_performance(funcao, *args):
    """Mede o tempo de execução e o número de comparações de uma função."""

    start_time = time.perf_counter() 
    resultado, comparacoes = funcao(*args)  # Executa a função
    tempo_execucao = time.perf_counter() - start_time  

    return resultado, comparacoes, tempo_execucao


def exibir_resultado(nome, indice, tempo, comparacoes, extra=""):
    print(f"➤ {nome}:")
    if indice != -1:
        print(f"Alvo encontrado no índice {indice}.")
    else:
        print("O alvo não está na lista.")
    print(f"Tempo: {tempo:.6f}s | Comparações: {comparacoes:,} {extra}\n")

# ===============================================================================
#                          FUNÇÃO PRINCIPAL DE EXECUÇÃO
# ===============================================================================
def main():
    """Função principal que orquestra todo o fluxo de execução."""
    
    caminho_dicionario = construir_caminho_arquivo('br-utf8.txt')

# -------------------------- CARREGAR DADOS --------------------------
    print(f"\nCarregando palavras do arquivo '{caminho_dicionario}'...")
    fonte_de_palavras = carregar_palavras_de_arquivo(caminho_dicionario)
    print(f"Arquivo carregado! Total de palavras únicas: {len(fonte_de_palavras)}")

    # Configurações para a simulação
    tamanho_lista_busca = 100_000
    lista_original = preparar_lista(fonte_de_palavras, tamanho_lista_busca)
    palavra_alvo = random.choice(lista_original) 

# ------------------------ EXECUTAR ALGORITMOS -------------------------
# Busca linear:
    indice_linear, comp_linear, tempo_linear = medir_performance(busca_linear, lista_original, palavra_alvo)
# Busca binária:
    lista_ordenada, comp_qs_busca, tempo_sort = medir_performance(quick_sort, list(lista_original.copy())) # ordenação
    indice_binario, comp_binaria, tempo_binario = medir_performance(busca_binaria, lista_ordenada, palavra_alvo)
   
# -------------------------- EXIBIR RESULTADOS -------------------------
    info_ordenacao = f"\nTempo de Ordenação: {tempo_sort:.6f}s | {comp_qs_busca:,} comparações"
    
    print("\n" + "═" * 60)
    print(f"  ✦ INICIANDO TESTES DE BUSCA (Lista com {tamanho_lista_busca:,} palavras) ✦")
    print("═" * 60)
    print(f"              Palavra alvo: '{palavra_alvo}' \n")
    
    exibir_resultado("Busca Linear", indice_linear, tempo_linear, comp_linear)
    exibir_resultado("Busca Binária", indice_binario, tempo_binario, comp_binaria, info_ordenacao)

    print(f"Tempo total da Busca Binária com ordenação): {tempo_binario + tempo_sort:.6f} segundos\n")
   

if __name__ == "__main__":
    main()