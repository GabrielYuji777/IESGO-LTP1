def primo(numero):
    if numero <= 1:
        return False
    else:
        for i in range(2, numero):
            if numero % i == 0:
                return False
        return True

numero = int(input("Digite um número inteiro: "))
if primo(numero):
    print(f"O número {numero} é primo.")
else:
    print(f"O número {numero} não é primo.")