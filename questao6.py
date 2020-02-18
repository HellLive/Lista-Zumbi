'''Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média
esperada para a viagem.'''

distancia = float(input('informe a distancia a ser percorrida: '))
velocidade= float(input('Velocidade a ser media da viagem: '))

prazo =  distancia/velocidade

print('O tempo aproximado de chega é %.2f minutos'%prazo)
