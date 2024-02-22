hexadecimal = input("Digite seu número para converter: ")

def hexadecimal_maior_10(num):
    if(num == "A"):
        return 10
    elif(num == "B"):
        return 11
    elif(num == "C"):
        return 12
    elif(num == "D"):
        return 13
    elif(num == "E"):
        return 14
    elif(num == "F"):
        return 15
    else:
        return int(num)
    

decimal = 0
i = len(hexadecimal)-1

for j in range(len(hexadecimal)):
    num = hexadecimal_maior_10(hexadecimal[j])
    print(num)
    decimal += num*(16**i)
    i = i-1

print(decimal)