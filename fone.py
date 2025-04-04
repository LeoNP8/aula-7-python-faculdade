print("Alo mundo")

num = int(input("Coloque um numero: "))
print(num)


a = int(input("Digite um numero para a: "))
b = int(input("Digite um numero para b: "))

print("A soma de 'a' + 'b' =", a + b)


nota1 = int(input("informe sua primeira nota: "))
nota2 = int(input("Informe sua segunda nota: "))
nota3 = int(input("informe sua terceira nota: "))
nota4 = int(input("Informe sua quarta nota: "))
media = (nota1 + nota2 + nota3 + nota4) / 4

num1 = int(input("Coloque o primeiro numero: "))
num2 = int(input("Coloque o segundo numero: "))

if num1 > num2:
    print("O primeiro numero é maior que o segundo")
else:
    print("O segundo numero é maior que o primeiro")
    
num1 = int(input("coloque o numero: "))
if num1 < 0:
    print("esse numero é negativo")
else:
    print("esse numero é positivo")
    
sobrenome = int(input("qual é o seu ultimo sobrenome: "))
print("sua familia é", sobrenome)

esporte = str(input("Qual o seu esporte favorito?: "))
print("o seu esporte favorito é", esporte)
    
print("Ciencias da computação")

profissao = str(input("Qual a sua profissão? "))
print("A sua profissão é", profissao)

idade = int(input("coloque sua idade: "))
print("sua idade é:", idade)

lado1 = float(input("Primeiro lado: "))
lado2 = float(input("Segundo lado: "))
lado3 = float(input("Terceiro lado: "))
lado4 = float(input("Quarta lado: "))

perimetro = lado1 + lado2 + lado3 + lado4

salario = float(input("Qual o seu salário: "))
comissao = salario * 0.05
print(comissao + salario)

distancia = float(input("qual é a distancia entre são Paulo e rio de janeiro? "))
print("A distancia é:", distancia)

#1- Faça um programa em Linguagem Python que leia um valor inteiro e mostre a tabuada de 1 a 10 do valor lido.
num = int(input('Qual numero você deseja ver a tabuada: '))

for c in range(1, 11):
    tabu = num * c
    print(f'{num} x {c} = {tabu}')

#2- Escreva um programa em Python que leia a cotação do dólar (taxa de conversão), leia um valor em dólares e converta e mostre o valor equivalente em Reais.
dol = 5.72
real = (float(input('Digite um valor em dolar para converter para real: U$')))
print(f'O valor do dolar esta U${dol} logo a conversão ficara R${real}')

#1- Escreva um programa em Python que leia um valor representando o gasto realizado por um cliente do restaurante ComaBem e visualize o valor total a ser pago, considerando os 10% do garçom.
valop = float(input('Digite o valor gasto no restalrante: '))
garcom = valop * (10 / 100)
print(f'O valor a se pagar com a taxa do garçom é de {valop + garcom}')

#2- Escreva um programa em Python que receba uma string do usuário e mostre de trás para frente
palavra = str(input('Digite uma palavra: ')).upper()
print(f'{palavra[::-1]}')
