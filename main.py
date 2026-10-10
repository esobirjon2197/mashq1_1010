# 15-m
numbers = [4, 7, 12, 15, 20, 9, 8]

juft_sonlar = []

for son in numbers:
    if son % 2 == 0:
        juft_sonlar.append(son)

print(juft_sonlar)



# 16-m
names = ["Ali", "Vali", "Sardor", "Madina", "Aziza", "Anvar"]

a_ismlar = []

for ism in names:
    if ism.startswith("A"):
        a_ismlar.append(ism)

print(a_ismlar)


# 17-m
fruits = ["olma", "banan", "anor"]

fruits.append("uzum")

print(fruits)


# 18-m
colors = ["qizil", "yashil", "ko‘k", "sariq"]

colors.remove("ko‘k")

print(colors)


# 19-m
colors = ["qizil", "yashil", "ko‘k", "sariq"]

colors.remove("ko‘k")

print(colors)


# 20-m
numbers = [17, 4, 25, 9, 12, 2]

numbers.sort()

print(numbers)
