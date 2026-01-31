lst = [] #Вставити дані в лист
a = lst.count(0)
while lst.count(0)>=1:
    lst.remove(0)
while a > 0:
    lst.append(0)
    a -= 1
print(lst)
