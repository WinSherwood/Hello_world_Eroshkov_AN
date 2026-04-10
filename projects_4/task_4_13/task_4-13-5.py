
n = int(input("Введите количество чисел N: "))

max = float(input("Введите число 1: "))

i = 2
while i <= n:
    x = float(input(f"Введите число {i}: "))
    if x > max:
            max = x
    i += 1  

    
print(f"Максимальное число: {max}")