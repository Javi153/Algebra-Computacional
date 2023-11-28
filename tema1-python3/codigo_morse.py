dicc = {"a" : ".-", "b" : "-...", "c" : "-.-.", "d" : "-..", "e" : ".",
"f" : "..-.", "g" : "--.", "h" : "....", "i" : "..", "j" : ".---", "k" :
"-.-", "l" : ".-..", "m" : "--", "n" : "-.", "o" : "---", "p" : ".--.",
"q" : "--.-", "r" : ".-.", "s" : "...", "t" : "-", "u" : "..-", "v" :
"...-", "w" : ".--", "x" : "-..-", "y" : "-.--", "z" : "--.." }

texto = "este es un texto de prueba para probar el diccionario"

n = len(texto)
i = 0
morse = ""
while i < n:
    letra = texto[i]
    if i != 0:
        morse += " "             # separador entre letras es " "
    if letra == " ":
        morse += " "             # separador entre palabras es "   "
    else:
        morse += dicc[letra]
    i += 1

print(morse)
