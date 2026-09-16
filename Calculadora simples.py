print("Calculadora simples: +,-,*,/")

a = float(input("Insira um número: \n"))

operacao = str (input("Operação (|+|-|*|/|)"))

b = float(input("Insira outro número: \n"))

if operacao == '+':
  print(a + b)

if operacao == '-':
    print(a - b)

if operacao == '*':
  print(a * b)


if operacao == '/':
  if b != 0:
    print(a / b)

  else:
    print("Não existe")
