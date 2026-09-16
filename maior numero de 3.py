# define o maior número escolhido entre 3 numeros
print ("Maior entre 3")

a = int (input("insira o primeiro número: "))
b = int (input("insira o segundo número: "))
c = int (input("insira o terceiro número: "))

if  a > b and a > c:
  print("Maior: ", a)

elif b > a and b > c:
  print("Maior: ", b)

else:
  print("Maior: ", c)
