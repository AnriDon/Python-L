time = int(input("Введить кількість хвилин \n"))
if time > 60:
    hour = time // 60
    minute = time - (hour * 60)
    print(hour, "годин", minute, "хвилин")
else:
    print(time, "хвилин")