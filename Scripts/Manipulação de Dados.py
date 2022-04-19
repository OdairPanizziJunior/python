print("="*30)                            # preenche uma linha com ""="" e neste caso foi 30
nome = input("Qual é seu nome? ")
print("Welcome {:=^13}".format(nome))    # quantos ""="" eu quero que fique na linha do nome contando com os caracteres do nome

n1 = int(input("Digite um Valor: "))
n2 = int(input("Digite outro valor: "))

print("A soma de", n1, "com", n2 ,"vale: {}".format(n1 + n2))
print("A subtração de", n1, "com", n2, "vale: {}".format(n1 - n2))
print("A multiplicação de", n1, "com", n2, "vale: {}".format(n1 * n2))
print("A exponenciaçaõ de", n1, "com", n2,"vale: {}".format(n1**n2))
print("A divisão Inteira de", n1, "com", n2, "vale: {}".format(n1 // n2), end="")
print("A divisão de", n1, "com", n2, "vale: {:.3f}".format(n1 / n2)) # 3 casas depois da vírgula -> {:.3f}