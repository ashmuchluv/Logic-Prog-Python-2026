print("Aumento de 15%")

salario = float (input("Salário: R$"))

aumento = input("Autorizado o aumento?")

if aumento.lower () == "sim" and salario <=2000:
  aumento = True
  aumento = salario * 0.15
  print ("Salário com aumento: R$", salario + aumento)
else:
  aumento = False
  print("Sem aumento. R$", salario)
