print (" Quem pode votar")

titulo = int (input("Possui título? 1 = sim/ 0 = não "))
idade = int (input("Idade: "))

if (titulo <= 0):
  print("Não pode votar")

elif (idade >=16):
  print("Pode votar")

else:
  print("Não pode votar")
