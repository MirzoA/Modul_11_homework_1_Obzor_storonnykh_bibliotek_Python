import requests
r = requests.get('https://mirzoa.github.io/resume/')
print(r.text)

# Считать данные из файла с помощью библиотеки pandas
import pandas as p
data = p.read_fwf(r'https://github.com/MirzoA/Modul_10_homework_1_Sozdanie_potokov/blob/'
                  r'main/Modul_10_homework_1_Sozdanie_potokov.py')
# Отображение первых 5 строк данных
print(data.head(5))
print()
print()
# Создать массив чисел с помощью библиотеки numpy

import numpy as n

arr = n.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
print(f'Вывод массива {arr}')
print(f'Вывод количества элементов массива [{arr.size}]')
print(f'Сумма элементов массива [{n.sum(arr)}]')
print(f'Возведение каждого элемента массива в квадрат {n.square(arr)}')

# Визуализировать данные с помощью библиотеки matplotlib

import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [4, 3, 8, 2, 11]
plt.plot(x, y)
plt.show()


#  Обработать изображение с помощью библиотеки pillow

from PIL import Image

img = Image.open('KINO.jpg')

# Изменяем размер изображения
resized_img = img.resize((512, 512))
img.show()
# Сохраняем обработанное изображение
resized_img.save('resized_image.jpg')

print("Изображение обработано и сохранено.")