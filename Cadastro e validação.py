print("Cadastro e validação: senha correta")

senha = str (input ("Informe a senha: \n"))

nvsenha = (input ("Repita a nova senha: \n"))

autenticacao = True

if senha == nvsenha and autenticacao:
  print("Autorizado!")
else:
  print("Não autorizado")
