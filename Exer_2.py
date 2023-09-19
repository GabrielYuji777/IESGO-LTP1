def contar_letra(letra):
    texto = input(" Escreva uma frase ").lower()
    return texto.count(letra)

letra_a_contar = 'a'
print("Nome contem ", contar_letra(letra_a_contar), " letras "+ letra_a_contar)