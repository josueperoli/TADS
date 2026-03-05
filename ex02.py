nomes = ["Josué", "Zé", "Trem", "coisa"]

print(nomes[0])
print(nomes[1])
print(nomes[2])
print(nomes[3])


print(f"Olá, {nomes[0]}")
print(f"Olá, {nomes[1]}")
print(f"Olá, {nomes[2]}")
print(f"Olá, {nomes[3]}")

nomes.append("huguinho")
print(nomes)

nomes.insert(0, "peninha")
print(nomes)

del nomes[1]
print(nomes)