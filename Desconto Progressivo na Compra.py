print ("Desconto Progressivo na Compra\n")


def principal ():

  valorcompra = float (input("Valor da compra: R$"))

  valorfinal = valordesconto (valorcompra)

  print ("Valor final: R$", valorfinal)


def valordesconto (valorcompra):

    if valorcompra >= 100 and valorcompra <= 299:
      return valorcompra * 0.90

    elif valorcompra >= 300 and valorcompra <= 499:
      return valorcompra * 0.85

    elif valorcompra >= 500:
      return valorcompra * 0.80

    else:
      print ("\nSem Desconto Aplicado")
      return valorcompra

principal ()
