def multiplo_de_5(numero):
    if numero % 5 == 0:
        return True
    else:
        return False
    
numero = int(input(" Digite um número inteiro "))
if multiplo_de_5(numero):
    print(f"O número {numero} é múltiplo de 5.")
else:
    print(f"O número {numero} Não é múltiplo de 5.")