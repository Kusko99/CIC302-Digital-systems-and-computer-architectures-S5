binario = input("Digite o número em binário para converte-lo: ")

i = len(binario) - 1
decimal = 0

for j in range(len(binario)):
    decimal += int(binario[j])*(2**i)
    i = i -1

print(decimal)

hexadecimal = []

def hexadecimal_maior_10(num):
    if(num == 10):
        return "A"
    elif(num == 11):
        return "B"
    elif(num == 12):
        return "C"
    elif(num == 13):
        return "D"
    elif(num == 14):
        return "E"
    elif(num == 15):
        return "F"
    else:
        return str(num)
    
while(decimal >= 16):
    num = decimal%16
    hexadecimal.append(hexadecimal_maior_10(num))
    decimal = decimal//16

hexadecimal.append(hexadecimal_maior_10(decimal))
hexadecimal.reverse()

print(hexadecimal)