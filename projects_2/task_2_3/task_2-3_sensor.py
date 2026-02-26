FIO = input('Введите имя оператора: ')
pressure = input('Введите текущее значение давления (Па)')

with open('sensor_log.txt', 'a', encoding='utf-8') as sensor:
    sensor.write(f'Имя оператора\t{FIO}\tДавление\t{pressure}')