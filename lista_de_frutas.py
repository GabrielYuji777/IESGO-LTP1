lista = []
while True:
    fruta = input("""Digite o nome de uma fruta ou digite "sair" """)
    if fruta == "sair":
        print(lista)
        break
    lista.append(fruta)
    print(lista)