lista =["a","b","c", 10]
print(lista)
print(lista[-1])
print("intervalo de items ",lista[1:3])
print("intervalo de items invertido ",lista[-4:])

for i in lista:
    print("item da lista ", i)

if "a" in lista:
    print("a tali")
else:
    print("a tali n")

print(len(lista))

lista.append("z")
print(lista)
lista.insert(1,"h")
print(lista)

lista.remove("a")
print(lista)

lista.pop(2)
print(lista)

del lista[1]
print(lista)

# del lista deleta a lista
print(lista)

lista.clear()
print(lista)

lista.append("a")
lista.append("b")
lista.append("c")
print(lista)

lista2 = lista.copy()
print(lista2)

lista3 = list(lista2)
print(lista3)

lista.append("a")
lista.append("a")
lista.append("a")
print(lista)
print(lista.count("a"))

print(lista.index("a")) #lugar do item