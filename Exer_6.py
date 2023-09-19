def Escrever_nome_sobrenome():
    nome = input(" Escreva o seu nome completo: ")
    partes_nome = nome.split( )
    primeiro_nome = partes_nome[0]
    sobrenome = " ".join(partes_nome[1:])

    return primeiro_nome.upper() +" "+ sobrenome.lower()

print(Escrever_nome_sobrenome())