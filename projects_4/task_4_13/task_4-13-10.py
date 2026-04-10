arr = [float(i) for i in input("Введите числа через пробел: ").split()]
sum = 0

for i in range(len(arr)):
    if i % 2 != 0:          
        sum += arr[i]     


print("Сумма элементов с нечётными индексами:", sum)