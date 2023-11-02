print('Olá Mundo!')
nome = input('Qual é o seu nome? ')
print('Olá {}! Prazer em te conhecer!'.format(nome))
dia = input('Qual dia você nasceu? ')
mes = input('Qual mês você nasceu? ')
ano = input('Qual ano você nasceu? ')
print('{}, você nasceu no dia {} do mês {} de {}. Correto?'.format(nome, dia, mes, ano))

print('Vamos somar um dois valores?')
numero1 = int(input('Primeiro número: '))
numero2 = int(input('Segundo número: '))

soma =numero1 + numero2

print('A soma é {}'.format(soma))
