bin1 = input("Digite o primeiro número: ")
bin2 = input("Digite o segundo número: ")


def converte_binario_decimal(binario):
    i = len(binario) - 1
    decimal = 0

    for j in range(len(binario)):
        decimal += int(binario[j])*(2**i)
        i = i -1

    print(decimal)
    return decimal

dec1 = converte_binario_decimal(bin1)
dec2 = converte_binario_decimal(bin2)

soma = dec1 + dec2

def converte_decimal_binario(decimal):
    
    binarylist = []

    while(decimal >= 2):
        binario = decimal%2
        binarylist.append(binario)
        decimal = decimal//2

    binarylist.append(decimal)
    binarylist.reverse()

    return binarylist

result = converte_decimal_binario(soma)
print(result)