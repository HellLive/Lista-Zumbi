'''Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a
porcentagem do aumento. Exiba o valor do aumento e do novo salário.'''

salario=int(input('Informe seu salario inicial:'))
porcent=float(input('Informe a porcentagem:'))

novo= salario*(porcent/100)
saldo=novo+salario

print('Teve um aumento no seu salario no valor de %3.2f' %novo)
print('Seu novo salário será de %d'%saldo)
