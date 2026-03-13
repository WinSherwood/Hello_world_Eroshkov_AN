#!/bin/bash
echo "Создание файлов:"
for i in {1..10}; do
    touch "test$i.txt"
    echo "Создан файл test$i.txt"
done

echo ""
echo "Удаление файлов в обратном порядке:"
num=10
while [ $num -ge 1 ]; do
    rm "test$num.txt"
    echo "Удален файл test$num.txt"
    num=$((num - 1))
done

echo ""
echo "Готово!"
