print("--Prática esportiva: 12 a 17 anos, autorização--")

idade = int(input("Idade: \n"))

autorizacao = input("Possui Autorização?\n").lower () == "sim"

if idade >=12 and idade <= 17 and autorizacao == True:
  print ("Autorizado")
else:
  print ("Não autorizado")
