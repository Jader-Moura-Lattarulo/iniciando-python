des = ' DESAFIO 05 '
print('{:=^30}'.format(des))
print('Qual número você quer saber o antecessor e o sucessor? ', end='')
numero = int(input())
ant = numero -1
suc = numero +1
print('O antecessor de {} é {};'.format(numero, ant))
print('Seu sucessor é {}.\n\n'.format(suc))

des = ' DESAFIO 06 '
print('{:+^30}'.format(des))
print('Qual número você quer saber o dobro, triplo e raiz quadrada? ', end='')
numero = int(input())
dob = numero * 2
tri = numero *3
raiz = pow(numero, 0.5)
print('O dobro é: {}, o triplo é: {} e a raiz quadrada é: {}\n\n'.format(dob, tri, raiz))

des = ' DESAFIO 07 '
print('{:!^30}'.format(des))
print('Insira o nome do aluno:', end=' ')
nome = str(input())
print('Insira foi a primeira nota:', end=' ')
nota01 = float(input())
print('Insira foi a segunda nota:', end=' ')
nota02 = float(input())

media = (nota01 + nota02)/2

print('O aluno {}, tirou as notas {} e {} e ficou com a média final: {:.2f}\n\n'.format(nome, nota01, nota02, media))

des = ' DESAFIO 08 '
print('{:#^30}'.format(des))
print('Quantos metros você quer converter para centimetros e milímetros?', end=' ')
metros = float(input())
cent = metros*100
mm = metros*1000
print('Conversão realizada, {} metro(s) é equivalente a {} centimetros e {} milímetros.\n\n'.format(metros, cent, mm))

des = ' DESAFIO 09 '
print('{:#^30}'.format(des))
print('Qual número você deseja saber a tabuada? ', end='')
num = int(input())
print('{} X {:2} = {}'.format(num, 1, num*1))
print('{} X {:2} = {}'.format(num, 2, num*2))
print('{} X {:2} = {}'.format(num, 3, num*3))
print('{} X {:2} = {}'.format(num, 4, num*4))
print('{} X {:2} = {}'.format(num, 5, num*5))
print('{} X {:2} = {}'.format(num, 6, num*6))
print('{} X {:2} = {}'.format(num, 7, num*7))
print('{} X {:2} = {}'.format(num, 8, num*8))
print('{} X {:2} = {}'.format(num, 9, num*9))
print('{} X {:2} = {}\n\n'.format(num, 10, num*10))

des = ' DESAFIO 010 '
print('{:#^30}'.format(des))

print('Quantos reais você quer converter para dólar? R$', end='')
reais = float(input())
dol = reais/4.95
print('O Dólar está equivalente a R$4,95, portanto você possui: ${:.2f}\n\'.format(dol))

des = ' DESAFIO 011 '
print('{:@^30}'.format(des))
print('Qual a largura da parede a ser pintada? ', end='')
larg = float(input())
print('Qual a altura da parede a ser pintada? ', end='')
alt = float(input())
parede = alt*larg
print('A parede possui {:.2f}m² e 1l de tinta pinta 2m² portanto você precisara de {} litros de tinta.\n\n'.format(parede, parede/2))

des = ' DESAFIO 012 '
print('{:~^30}'.format(des))

print('Quanto custa o produto? R$', end='')
preco = float(input())
print('Com o desconto de 5% o produto passa a valer: R${:.2f}\n\n'.format(preco-(preco/100)*5))

des = ' DESAFIO 013 '
print('{:/^30}'.format(des))

print('Qual é o seu atual salário? R$', end='')
salario = float(input())
print('Com os 15% de aumento você passa a receber: R${:.2f}'.format(salario+(salario/100)*15))