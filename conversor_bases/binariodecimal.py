binario = input("Digite o número em binário para converte-lo: ")

i = len(binario) - 1
decimal = 0

for j in range(len(binario)):
    decimal += int(binario[j])*(2**i)
    i = i -1

print(decimal)