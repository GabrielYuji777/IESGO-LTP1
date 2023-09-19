def palindromo (palavra):
    palavra = palavra.lower(). replace(" ", "")
    return palavra == palavra[::-1]

entrada = input("Digite uma palavra:")

if palindromo(entrada):
    print(f"{entrada} é um palíndromo!")
else:
    print(f"{entrada} não é um palíndrome.")