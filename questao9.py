***Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo
usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar,
sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.***

x=int(input("Qual a quantidade de KM percorrido com o carro:"))
y=int(input("Quantidade de dias utilizado pelo carro:"))

pagar = (y*60)+(x*0.15)
print("Valor a ser pago é de R$%5.2f"%pagar)
