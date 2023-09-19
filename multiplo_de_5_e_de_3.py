def multiplo_de_5(numero):
    if numero % 5 == 0:
        return True
    else:
        return False


def multiplo_de_3(numero):
    if numero % 3 == 0:
        return True
    else:
        return False


numero = int(input("Digite um número inteiro: "))
if multiplo_de_5(numero) and multiplo_de_3 (numero):
    print(f" O número {numero} é múltiplo de 5 e de 3.")
elif multiplo_de_5(numero):
    print(f" O número {numero} é múltiplo de 5. ")
elif multiplo_de_3(numero):
    print(f" O número {numero} é multiplo de 3. ")
else:
    print(f" O número {numero} não é multiplo de 5 e nem de 3.")