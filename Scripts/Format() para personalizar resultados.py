nome = input("Nome: ")
print("Bem Vindo -> ", end="")
print(nome)

print("="*30)
print("OPERADORES")
print("="*30)
n1 = int(input("Digite um número inteiro: "))
s = n1 + 1
a = n1 - 1
d = n1 * 2
t = n1 * 3
r = n1 ** (1/2)

print("Sucessor de {} é {} e antecessor é {}".format(n1,s,a))
print("O sobro de {} é {}".format(n1,d))
print("O triplo de {} é {}".format(n1,t))
print("A Raiz quadrada de {} é {}".format(n1,r))

print("="*30)
print("MEDIA DE NOTAS")
print("="*30)
nota1 = int(input("Digite nota 1 "))
nota2 = int(input("Digite nota 2 "))
soma = nota1 + nota2
media = soma / 2

print("Total {}".format(soma))
print("Media {}".format(media))

print("="*30)
print("CONVERTER MEDIDAS")
print("="*30)
metrocru = float(input("Digite quantos metros quiser: "))
metro = int(metrocru)
c = int(metro * 100)
m = int(metro *1000)
print("O valor {} em centímetros é {}".format(metro, c))
print("O valor {} em milímetros é {}".format(metro,m))

print("="*30)
print("TABUADA")
print("="*30)
tabu = int(input("Digite o número a ser calculado: "))
print("A tabuada de {} é:".format(tabu))
print(tabu, "X 1 = {}".format(tabu*1))
print(tabu, "X 2 = {}".format(tabu*2))
print(tabu, "X 3 = {}".format(tabu*3))
print(tabu, "X 4 = {}".format(tabu*4))
print(tabu, "X 5 = {}".format(tabu*5))
print(tabu, "X 6 = {}".format(tabu*6))
print(tabu, "X 7 = {}".format(tabu*7))
print(tabu, "X 8 = {}".format(tabu*8))
print(tabu, "X 9 = {}".format(tabu*9))
print(tabu, "X 10 = {}".format(tabu*10))

print("="*30)
print("CÂMBIO")
print("="*30)
dol = float(input("Eai, quanto tens na carteira em R$? "))
print("Cotação: $1,00 = R$3,27")
print("Com R${} você pode comprar apenas ${:.2f} Dólares".format(dol, dol/3.27))

print("="*30)
print("PINTURA")
print("="*30)
largura = float(input("Quantos metros de largura: "))
altura = float(input("Quantos metros de altura: "))
area = largura * altura
print("A parede tem {:.2f} metros quadrados".format(area))
print("Um litro de tinta pinta em tonro de 2m quadrados, então irá precisar de {:.2f} litros de tinta.".format(area/2))

print("="*30)
print("SALÁRIO")
print("="*30)
salario = float(input("Digite seu Salário:"))
print("Parabéns, você ganhou 15% de aumento!!!")
porc = 15/100
atual = (porc*salario)
print("Agora seu salário é de R${:.2f}".format(atual+salario))


print("="*30)
print("DESCONTO")
print("="*30)
preco = float(input("Quanto Custa?:"))
print ("Valor a vista > -5% de desconto")
porc = 5/100
atual = (porc*preco)
print("Total R${:.2f}".format(preco-atual))
