lst = [] #Вставити дані в лист
a = int(len(lst)/2)
if len(lst) % 2 != 0:
    a = a + 1
first = lst[:a]
second = lst[a:]
print(first, second)
