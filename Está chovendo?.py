print("Está chovendo?\n")

resposta = input ("Está chovendo? sim/não/yes/not\n").lower()

chovendo = resposta

if chovendo == "yes" or chovendo == "sim":
  print("Lembre-se do guarda-chuva")

elif chovendo == "not" or chovendo == "não":
  print("Pode sair sem o guarda-chuva.")
