decimal = int(input("Digite o número em decimal para converte-lo: "))
print(decimal)

binarylist = []

while(decimal >= 2):
    binario = decimal%2
    binarylist.append(binario)
    decimal = decimal//2

binarylist.append(decimal)
binarylist.reverse()

print(binarylist)