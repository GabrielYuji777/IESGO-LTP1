def calcular_signo(ano_nascimento):
    signos_chineses = ["Rato", "Boi", "Tigre", "Coelho", "Dragão", "Serpente", "Cavalo", "Cabra", "Macaco", "Galo", "Cachorro", "Porco"]
    
    ano_base = 1900  

    indice_signo = (ano_nascimento - ano_base) % 12

    return signos_chineses[indice_signo]


ano_nascimento = int(input("Digite o ano de nascimento: "))

signo = calcular_signo(ano_nascimento)
print(f"Seu signo chinês é {signo}")