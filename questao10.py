'''Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a
quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante
perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o
total de dias.'''


x=int(input("Quantidade de cigarros fumados por dias:"))
y=int(input("Quantidade de anos fumando o cigarro:"))

ano= (y*365)*x
perda= (ano*10)/24


print("Você perdeu equivalente a %d dias da sua vida"%perda)
