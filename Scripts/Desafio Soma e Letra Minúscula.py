#DESAFIO UM
print("DESAFIO 1")
print("")
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
s = n1+n2
print("")
print("A soma de", n1, "+", n2, "é", s)
print("A soma de {} + {} é {}".format(n1,n2,s))
print("")

#DESAFIO DOIS
print("DESAFIO 2")
n = input("digite algo: ") 
print(n.islower(), ", pois está em letra minúscula") #Se letras minúsculas, retorna TRUE
print(n.isnumeric(), ", pois NÃO é um número" ) #retorna FALSE e exibe a mensagem se "n" receber Letras.
