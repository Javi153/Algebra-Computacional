# queremos determinar cuántos de los 100 posibles números entre 00 y
# 99 aparecen como los dos últimos dígitos de los números 3^i para
# i=1,..,5000

# generamos los 5000 numeros (3^i mod 100) y los vamos agregando al
# conjunto nums
nums = set()                  # empezamos con nums = conjunto vacío
i = 1
while i <= 5000:
   nums |= {(3 ** i) % 100}   # la | es la union de conjuntos
   i += 1

# imprimimos el conjunto nums y su cantidad de elementos
print(nums)
print(len(nums))
