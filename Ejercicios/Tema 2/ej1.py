#Casos base
#x = 0 o y = 0, entonces (a, b) = (0, 1) o (a, b) = (1, 0)

#Si ambos son pares, el gcd de x/2, y/2 sera la mitad que el de x, y por tanto si 
#gcd(x/2, y/2) = a' * x/2 + b' * y/2 => gcd(x, y) = a' * x + b' * y

#Si x par y impar puede ser que a' sea par o impar. Si a' es par, simplemente a*x/2 pasa a ser a/2 * x
# Si a' es impar tendremos x * ((a' + y)/2) + y*(b' - x/2)
