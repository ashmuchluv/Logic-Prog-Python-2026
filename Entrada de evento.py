print("Entrada de evento: +18 e ingresso")

idade = int (input("Informe sua idade: \n"))

ingresso = (input("Possui ingresso? sim/não\n")).lower() == 'sim'

ingresso == True

if idade >=18 and ingresso == True:
  print("Pode entrar no evento")

else:
  print("Não pode entrar")
