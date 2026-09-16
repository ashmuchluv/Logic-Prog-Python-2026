print ("Compra a vista 10%")

valor = float(input("Valor da compra: R$"))
avista = input("Compra à vista?")

if avista.lower() == "sim":
  avista = True
  desconto = valor * 0.10
  print("Valor final: R$", valor - desconto)

else:
  avista = False
  print("Sem desconto", valor)
