def quantidade(texto):
    texto_sem_espaca = texto.lower().replace(' ', '')
    return len(texto_sem_espaca)
 
    
print(" Esse texto possui ",quantidade(input(" Escreva um texto ")), " caracteres ")