import random

palavras = ['algoritmo', 'python']
vida = 6
jogadas = ""
palavra = random.choice(palavras)
tela = ["_" for _ in palavra]

while vida > 0:
    print("Palavra:", " ".join(tela))
    print("Vidas restantes:", vida)
    print("Letras já jogadas:", " ".join(jogadas))

    letra = input("Digite uma letra: ").lower()

    if letra in jogadas:
        print("Você já tentou essa letra!")
        continue

    jogadas += letra

    if letra in palavra:
        print("A letra está na palavra.")
        for i, l in enumerate(palavra):
            if l == letra:
                tela[i] = letra
    else:
        print("A letra não está na palavra.")
        vida -= 1

    if "_" not in tela:
        print("Você ganhou! A palavra era:", palavra)
        break
else:
    print("Você perdeu! A palavra era:", palavra)