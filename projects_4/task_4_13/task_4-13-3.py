 
n = int(input("Введите число N: "))

factorial = 1
i = 1

while i <= n:
    factorial = factorial * i
    i = i + 1

# 🔹 Блок "Вывод" (параллелограмм)
print(f"Факториал {n}! = {factorial}")