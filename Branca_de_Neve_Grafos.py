def mostrar_cena(cena, escolhas):
    print(f"\n{cena}")
    for i, escolha in enumerate(escolhas, start=1):
        print(f"{i}. {escolha}")
    opcao = input("\nEscolha uma opção: ")
    return opcao

# Dicionário de Cenas
cenas = {
    0: "INÍCIO: Madrasta pergunta ao espelho se há alguém mais bela que ela.",
    1: "CENA 2: Caçador da Madrasta é enviado para matar a Branca de Neve.",
    2: "CENA 3: Branca de Neve encontra a casa dos anões.",
    3: "CENA 4: Anões aceitam Branca de Neve em sua casa. A bruxa oferece uma maçã para a Branca de Neve.",
    4: "CENA 5: Branca de Neve dorme.",
    5: "CENA 6: Colocaram ela na caixa de vidro.",
    6: "CENA 7: Príncipe beija a Branca de Neve e a pede em casamento.",
}

escolhas = {
    0: ["O espelho mente.", "O espelho diz a verdade."],
    1: ["O caçador mata a branca de neve.", "O caçador deixa a branca de neve viver."],
    2: ["Branca de neve bagunça a casa.", "Branca de neve arruma a casa."],
    3: ["Branca de neve guarda a maçã.", "Branca de neve come a maçã."],
    4: ["Anões enterram a branca de neve.", "Anões colocam a branca de neve em uma caixa de vidro."],
    5: ["Branca de neve é encontrada pelo caçador.", "Branca de neve é encontrada pelo príncipe."],
    6: ["Branca de neve não foi feliz com o príncipe.", "Branca de neve foi feliz."]
}

finais = {
    0: "PRIMEIRO FIM: Branca de neve continua como escrava da rainha até o fim de sua vida.",
    1: "SEGUNDO FIM: O Caçador mata a Branca de Neve.",
    2: "TERCEIRO FIM: Os anões ficam revoltados e mandam Branca de Neve embora. Ela acaba morrendo atacada pelos animais da floresta.",
    3: "QUARTO FIM: Branca de Neve faz uma torta com a maçã envenenada. Os anões e a Branca de Neve comem e dormem para sempre na floresta.",
    4: "QUINTO FIM: Branca de Neve se transforma numa vampira e morde os anões, que também se tornam vampiros.",
    5: "SEXTO FIM: Branca de Neve se casa com o caçador, mas se divorcia após ele fazer ensopado com os animais da floresta. Então, ela vira veterinária.",
    6: "SÉTIMO FIM: Branca de Neve não se adapta à vida na corte, se divorcia e volta a morar com os 7 anões.",
    7: "OITAVO FIM: Branca e o Príncipe vivem felizes para sempre."
}

finais = {}

# Matriz de Adjacência (Grafo)
grafo = [
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # Início
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # Primeiro final
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # Cena 2
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # Segundo fim
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0], # Cena 3
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # Terceiro fim
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0], # Cena 4
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # Quarto fim
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0], # Cena 5
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # Quinto fim
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0], # Cena 6
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # Sexto fim
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], # Cena 7
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # Sétimo fim
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # Oitavo fim 
]

def iniciar_jogo():
    print("\n================== Branca de Neve e as Sete Versões ==================\n")
    posicao = 0
    while True:
        print(cenas[posicao])
        conexoes = [i for i, val in enumerate(grafo[posicao]) if val == 1]
        if not conexoes:  # Sem conexões, fim de jogo
            print("\nFim de jogo!")
            break
        print("Escolhas:")
        for i, conexao in enumerate(conexoes, start=1):
            print(f"{i}. {cenas[conexao]}")
        escolha = int(input("\nEscolha uma opção: ")) - 1
        posicao = conexoes[escolha]

if __name__ == "__main__":
    iniciar_jogo()
