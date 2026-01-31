lst = [] #Вставити дані в лист
# Sum = []
# v = 0
# result = 0
# if lst == []:
#    print(v)
# for a, b in enumerate(lst):
#     if a % 2 == 0 or a == 0:
#         Sum.append(b)
# for s in Sum:
#     v = v + s
#     result = v * lst[-1]
# if lst != []:
#     print(result)
#Тут я відчув шо якось багато всього і складним шляхом пішов, тож почав ресерчити
if lst:
    result = sum(lst[::2]) * lst[-1]
    print(result)
else:
    print(0)
