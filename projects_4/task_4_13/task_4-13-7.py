arr = [float(i) for i in input("Введите числа через пробел: ").split()]

s = 0
for x in arr:
    s = s + x

srednee = s / len(arr)


print("Среднее арифметическое:", srednee)