amigos = ["Huguinho", "Zezinho", "Luizinho", "Zezinho"]

#Ordenação - Case sensitive (letras minusculas < maiusculas)
amigos.sort()
#print(amigos)

#Ordenação case insensitive (não importa se é maiuscula ou minuscula, vai colocar em ordem)
amigos.sort(key = str.lower)
#print(amigos)

amigos = ["Huguinho", "Zezinho", "Luizinho", "Zezinho"]
print(sorted(amigos, reverse=True, key=str.upper))#cria uma lista com invertida, não sensitive
print(amigos)

