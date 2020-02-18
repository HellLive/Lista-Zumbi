'''Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule
o total em segundos.'''

dias=int(input('Digite a quantidades de dias:'))
horas=int(input('Digite a quantidades de horas:'))
minutos=int(input('Digite a quantidades de dias:'))
seg=int(input('Digite a quantidades de segundos:'))

total=(dias*30*12*60*60)+(horas*60*60)+(minutos*60)+seg
print('A quantidade em segundos %d'%total)
