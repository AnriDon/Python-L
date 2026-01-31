from statistics import mean

u1 = float(input("""Необхідно ввести 3 числа.
Введіть число 1
"""))
print("Введіть число 2")
u2 = float(input())
print("Введіть число 3")
u3 = float(input())
a = u1, u2, u3
print(round(mean(a), 1))
