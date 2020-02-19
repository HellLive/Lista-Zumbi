'''Determine se um ano é bissexto. Verifique no Google como fazer isso
... Basicamente é um ano com um dia a mais 366 dias no caso'''

print("Descubra se o ano atual ele será ou não bissexto ")
ano=int(input("Qual o ano atual:"))

if ano % 4==0:
        print("é um ano bissexto")
else:
        print("Ano não bissexto")

