'''Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser
um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.'''

print("Infome a baixo os lados composto do triângulo")
x=int(input("Informe o lado de baixo:"))
y=int(input("Informe o lado esquerdo:"))
z=int(input("Informe o lado direito:"))

if x==z and y==z:
    print("Triangulo equilátero")
elif y==z:
    print("Triângulo isósceles")
else:
    print("Triângulo escaleno")
