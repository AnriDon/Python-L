a = float(input("Введіть перше число \n"))
b = float(input("Введіть друге число \n"))

op = input("Оберіть бажану дію +,-,/ або * \n")
if op == "+":
    print(a + b)
if op == "-":
    print(a - b)
if op == "*":
    print(a * b)
if op == "/" and b == 0:
    print("Ділення на 0 неможливе")
if op == "/" and b != 0:
    print(a / b)
