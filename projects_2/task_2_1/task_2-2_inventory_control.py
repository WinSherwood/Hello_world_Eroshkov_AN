reagent_name = input("Введите название нового реактива: ")
reagent_amount = input("Введите количество реактива(целое число): ")
print(f"Реактив {reagent_name} поступил на склад в количестве {reagent_amount} шт.")

with open('inventory.txt', 'a', encoding='utf-8') as file:
    file.write(f'Реактив {reagent_name} поступил на склад в количестве {reagent_amount} шт.\n')