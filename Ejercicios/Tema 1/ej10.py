#Javier Jimenez Arenas
def number2word(p, n):
    word = "" #palabra resultado
    l = [-1] * n #Hacemos una lista que contendrá los códigos ASCII de los caracteres resultado
    div = (26 ** n - 1) // 25 #El resultado de la serie geométrica 1+26+...+26^(n-1), que será el número de palabras con n-1 letras o menos
    j = 0
    while p > 0 and j < n: #Vamos a ir restando a p conforme saquemos las letras de izquierda a derecha, si p llega a 0 entonces ya tenemos la palabra
        p -= 1 #En la primera vuelta ajustamos para que las posiciones del diccionario comiencen en 0. 
        #En el resto de vueltas, si p > 0, significará que aún quedan letras por calcular por lo que la palabra no termina ahí y debemos eliminar la posibilidad de que la proxima letra sea vacia, por eso hacemos -= 1
        l[j] = p // div #Si nos quedan por calcular n - j letras, div representa el número de palabras con n - j - 1 letras o menos. Al dividir obtenemos un cociente entre 0 y 25 que corresponde a la próxima letra a calcular, 
        #pues a cada primera letra le corresponden div posibilidades de palabras con n - j - 1 letras a continuacion
        p = p % div #Para las letras que quedan por calcular usamos el resto de la division, que estará entre 0 y div - 1
        div //= 26 #Modificamos div para representar el número de palabras que pueden crearse con una letra menos que antes
        j += 1 #Aumentamos el contador
    for j in range(0, n):
        if l[j] != -1: #Si l[j] vale -1 es que ese espacio es vacío
            word += chr(ord('a') + l[j]) #Sino escribimos la letra correspondiente a partir de su código ASCII relativo a 'a'
    return word

def word2number(w, n):
    pos = 0
    div = (26 ** n - 1) // 25 #Igual que en la funcion anterior
    for i in range(0, len(w)):
        pos += (ord(w[i]) - ord('a')) * div + 1 #Realizamos la funcion inversa, ahora queremos el producto entre div y la posicion que corresponde a la letra. Además, ajustamos con el +1 para los posibles espacios vacíos
        div //= 26
    return pos


print(number2word(3, 1))
print(number2word(3, 2))
print(number2word(3, 100))
print(number2word(138096, 4))
print(word2number("ejemplo", 10))
print(word2number("estabapensandoenunejemplobastantelargoynosemeocurriaqueponer", 1000))