num = int(input("""Введіть ціле 4-х значне число
"""))
if num > 999 and num < 10000:
    a = num // 1000
    b = (num // 100) % 10
    c = (num // 10) % 10
    d = num % 10

    print(a)
    print(b)
    print(c)
    print(d)
else:
    print("Ви ввели не 4-х значне число")

