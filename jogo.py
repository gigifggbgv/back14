import random

# Lista de temas e palavras (Corrigida e Expandida)
temas = {
    "jogos": [
        "minecraft", "zelda", "roblox", "fortnite", "valorant",
        "freefire", "fifa", "pes", "mario", "sonic", "pokemon",
        "godofwar", "gta", "callofduty"
    ],
    "filmes": [
        "avatar", "matrix", "batman", "frozen", "moana", "shrek",
        "toystory", "carros", "minions", "transformers", "harrypotter",
        "jurassicpark"
    ],
    "animais": [
        "cachorro", "gato", "elefante", "girafa", "leao", "tigre",
        "baleia", "golfinho", "tubarao", "coruja", "macaco"
    ],
    "paises": [
        "brasil", "argentina", "portugal", "franca", "japao",
        "canada", "australia", "italia", "espanha", "mexico"
    ]
}

def escolher_palavra():
    """Mostra os temas e deixa o jogador escolher um deles."""
    print("Temas disponíveis:")
    print("1 - Jogos")
    print("2 - Filmes")
    print("3 - Animais")
    print("4 - Paises")
    print("5 - Aleatório")
    
    opcao = input("Escolha o número do tema: ")
    
    if opcao == "1":
        tema = "jogos"
    elif opcao == "2":
        tema = "filmes"
    elif opcao == "3":
        tema = "animais"
    elif opcao == "4":
        tema = "paises"
    else:
        tema = random.choice(list(temas.keys())) 
        
    palavra = random.choice(temas[tema])
    return tema, palavra

def mostrar_palavra(palavra, letras_acertadas):
    """Mostra a palavra com as letras já acertadas."""
    resultado = ""
    for letra in palavra:
        if letra in letras_acertadas:
            resultado += letra + " "
        else:
            resultado += "_ "
    return resultado

def jogar():
    print("=" * 40)
    print(" JOGO DA FORCA - PYTHON")
    print("=" * 40)
    
    # Agora chama a função que pede para escolher o tema
    tema_escolhido, palavra_secreta = escolher_palavra()
    
    letras_acertadas = []
    letras_tentadas = []
    vidas = 6
    pontos = 0
    
    print()
    print("Tema:", tema_escolhido)
    print("Descubra a palavra secreta!")
    print("Você tem", vidas, "vidas.")
    print()
    
    while vidas > 0:
        print("Palavra:", mostrar_palavra(palavra_secreta, letras_acertadas))
        print("Letras já tentadas:", letras_tentadas)
        print("Vidas:", vidas)
        print("Pontos:", pontos)
        print("-" * 40)
        
        letra = input("Digite uma letra: ").lower()
        
        # Validação da entrada
        if len(letra) != 1:
            print("Digite apenas UMA letra.")
            print()
            continue
        if not letra.isalpha():
            print("Digite apenas letras.")
            print()
            continue
        if letra in letras_tentadas:
            print("Você já tentou essa letra.")
            print()
            continue
            
        letras_tentadas.append(letra)
        
        if letra in palavra_secreta:
            print("Boa! A letra existe na palavra.")
            letras_acertadas.append(letra)
            pontos += 10
        else:
            print("Ops! Essa letra não está na palavra.")
            vidas -= 1
            pontos -= 2
        print()
        
        # Verifica se o jogador venceu
        venceu = True
        for letra_da_palavra in palavra_secreta:
            if letra_da_palavra not in letras_acertadas:
                venceu = False
                
        if venceu:
            print("=" * 40)
            print("PARABÉNS! VOCÊ VENCEU!")
            print("A palavra era:", palavra_secreta)
            print("Pontuação final:", pontos)
            print("=" * 40)
            break
            
    if vidas == 0:
        print("=" * 40)
        print("FIM DE JOGO!")
        print("A palavra era:", palavra_secreta)
        print("Pontuação final:", pontos)
        print("=" * 40)

# Início do programa
jogar()
