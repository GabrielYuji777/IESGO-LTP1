def substituir_vogais():
    frase = input(" Escreva uma palavra ")
    return frase.lower().replace('a', '?!').replace('e', '?!').replace('i', '?!').replace('o', '?!').replace('u', '?!')

print(substituir_vogais())