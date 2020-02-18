'''Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o
preço a pagar.'''

produto=float(input("Informe o valor do produto:"))
desconto=int(input("Informe o valor do desconto:"))

pagar=produto-(desconto/100)
novo=desconto/100

print("o valor do produto a se pagar é R$%3.2f"%pagar)
print('o valor do desconto é R$%2.2f'%novo)
