import random

numero_aleatorio = random.randint(1, 10)

while True:
    
    try:
        numero = int(input("Adivinhe um número entre 1 e 10: "))
        
        if 1 <= numero <= 10:
            break
        else:
            print("Por favor, insira um número válido entre 1 e 10.")
    except ValueError:
        print("Por favor, insira um número válido entre 1 e 10.")

if numero == numero_aleatorio:
    print("Você acertou!")
else:
    print(f"Você errou!")