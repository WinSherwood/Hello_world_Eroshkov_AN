#!/bin/bash

file="settings.php"

if [ ! -f "$file" ]; then
    echo "Ошибка: Файл $file не найден в текущей директории."
    exit 1
fi

sed -i 's|/var/lib/mysql/data|/mnt/ssd/mysql|g' "$file"

echo "Путь к базе данных в файле $file успешно обновлен."
exit 0
