import os

# Caminho da pasta onde os arquivos das cenas estarão armazenados
SCENES_PATH = "scenes"

escolhas = {
    0: [
        "O espelho mente e responde que a Rainha continua sendo a mais bela do reino.", 
        "O espelho diz a verdade e revela que há alguém mais bela do que ela."
       ],
    1: [
        "O caçador mata a Branca de Neve.",
        "O caçador deixa a Branca de Neve viver."
        ],
    2: [
        "Branca de Neve bagunça a casa.",
        "Branca de Neve arruma a casa."
       ],
    3: [
        "Branca de Neve guarda a maçã.",
        "Branca de Neve come a maçã."
        ],
    4: [
        "Anões enterram a Branca de Neve.",
        "Anões colocam a Branca de Neve em uma caixa de vidro."
        ],
    5: [
        "Branca de Neve é encontrada pelo caçador.",
        "Branca de Neve é encontrada pelo príncipe."
        ],
    6: [
        "Branca de Neve não foi feliz com o príncipe.",
        "Branca de Neve foi feliz."
        ]
}

# Grafo representado como um dicionário de listas de adjacência
grafo = {
    0: [7, 1],  
    1: [8, 2],  
    2: [9, 3],  
    3: [10, 4],  
    4: [11, 5],  
    5: [12, 6],  
    6: [13, 14]  
}

def carregar_cena(numero_cena):
    """Lê o arquivo da cena correspondente e retorna seu conteúdo."""
    caminho_arquivo = os.path.join(SCENES_PATH, f"{numero_cena}.txt")

    if not os.path.exists(caminho_arquivo):
        return f"Cena {numero_cena} não encontrada."

    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        return arquivo.read()

def iniciar_jogo():
    print("\n================== Branca de Neve e as Sete Versões ==================\n")
    print("PRÓLOGO\n")
    print("\n" + carregar_cena("PROLOGO")) 
    print("\n================== Branca de Neve e as Sete Versões ==================\n")
    posicao = 0

    while posicao in grafo:  # Continua enquanto não alcançar um fim
        print("\n" + carregar_cena(posicao))

        print("\nEscolhas:")
        print(f"1. {escolhas[posicao][0]}")
        print(f"2. {escolhas[posicao][1]}")
        escolha = int(input("\nEscolha uma opção: ")) - 1

        posicao = grafo[posicao][escolha]  # Atualiza a posição no grafo

    print("\n" + carregar_cena(posicao))  # Exibe o final
    print("\nFim de jogo!")

if __name__ == "__main__":
    iniciar_jogo()
