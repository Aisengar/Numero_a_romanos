
numeros_romanos = [(1000, 'M'),(900, 'CM'),(500, 'D'),(400, 'CD'),(90,'XC'),(50, 'L'), 
                 (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
def probar_nombre(numero):
    if numero <= 0:
        pass
    elif numero >4000:
        pass

def convertir_a_romano(numero):
    n_romano = ''
    while numero > 0 :
        for i, r in numeros_romanos:
            while numero >= i:
                n_romano += r
                numero -= i
    
    return n_romano

print(convertir_a_romano(3999))
print(convertir_a_romano(500))
print(convertir_a_romano(1))