print ("Opções/Escolha de forma de pagamento")

def principal ():
  print ("1 - Dinheiro")
  print ("2 - Cartão de Crédito")
  print ("3 - Cartão de Débito")
  print ("4 - Pix")
  print ("5 - Boleto")

  opcao = int (input("Escolha uma forma de pagamento: "))

  pagamento = escolhapagamento (opcao)

  print ("Forma de Pagamento: ", pagamento)

def escolhapagamento (opcao):

  match opcao:
    case 1:
      return "Dinheiro"
    case 2:
      return "Cartão de Crédito"
    case 3:
      return "Cartão de Débito"
    case 4:
      return "Pix"
    case 5:
      return "Boleto"
    case _:
      return "Opção inválida"

principal ()
