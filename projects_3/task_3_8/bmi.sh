#!/bin/bash

read -p  "Введите ваш вес (в кг): " WEIGHT
read -p "Введите ваш рост (в метрах): " HEIGHT

BMI=$(echo "scale=0; $WEIGHT / ($HEIGHT * $HEIGHT)" | bc )

echo "Индекс массы вашего тела: $BMI"
