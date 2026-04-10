arr = [float(i) for i in input("Введите числа через пробел: ").split()]


sum = 0

for x in arr:
    if x % 2 != 0:     
        sum += x      

print("Сумма нечетных чисел:", sum)