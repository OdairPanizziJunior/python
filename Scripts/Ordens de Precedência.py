print("Operadores aritméticos")
print("")
n1 = int(input("Digite o primeiro Número: "))
n2 = int(input("Digite o segundo Número: "))

soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2
exp = n1 ** n2
divint = n1 // n2
restdiv = n1 % n2

print("A soma de {} com {} dá {}".format(n1,n2,soma))
print("A subtração de {} com {} dá {}".format(n1,n2,sub))
print("A multiplicação de {} com {} dá {}".format(n1,n2,mult))
print("A divisão de {} com {} dá {}".format(n1,n2,div))
print("O número {} elevado {} dá {}".format(n1,n2,exp))
print("A divisão inteira de {} com {} dá {}".format(n1,n2,divint))
print("O resto da divisão entre {} e {} dá {}".format(n1,n2,restdiv))

print("")
print("+------------------------------+")
print("|Ordem de precedência em Python|")
print("+------------------------------+")
print("")
print("1 - primeiro os Parênteses () ")
print("2 - exponênciação ** ")
print("3 - operadores aritiméticos *  /  //  %")
print("4 - operadores + e -")