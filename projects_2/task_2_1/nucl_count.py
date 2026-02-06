print("=== Анализ последовательности ДНК ===")
dna = input("Введите последовательность ДНК: ").upper()

# Подсчёт A, T, G, C

count_A = dna.count("A")
count_T = dna.count("T")
count_G = dna.count("G")
count_C = dna.count("C")

print("Подсчёт нуклеотидов:")

print(f"A: {count_A}")
print(f"T: {count_T}")
print(f"G: {count_G}")
print(f"C: {count_C}")

print(f"Общая длина: {len(dna)} нуклеотидов")

print("=== Процентное содержание каждого из нуклеотидов ===")
print(f"Нуклеотид A: {round(count_A/len(dna)*100,1)} процентов")
print(f"Нуклеотид T: {round(count_T/len(dna)*100,1)} процентов")
print(f"Нуклеотид G: {round(count_G/len(dna)*100,1)} процентов")
print(f"Нуклеотид C: {round(count_C/len(dna)*100,1)} процентов")