arr = [float(i) for i in input("Введите числа через пробел: ").split()]
sum = 0
count = 0

for i in range(len(arr)):
    if i % 2 == 0:          
        sum += arr[i]     
        count += 1          


avg = sum / count
print("Среднее арифметическое (чётные индексы):", avg)
