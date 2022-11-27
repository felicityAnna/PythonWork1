# # Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

import math

x_os_A = float (input ('Введите координату точки А по оси Х: '))
y_os_A = float (input ('Введите координату точки А по оси Y: '))
x_os_B = float (input ('Введите координату точки B по оси Х: '))
y_os_B = float (input ('Введите координату точки B по оси Y: '))

# distance = (x_os_B - x_os_A) ** 2 + (y_os_B - y_os_A) ** 2
# distance = math.sqrt (distance)
# distance = int (distance * 100)
# distance = float (distance / 100)
distance = float((int((math.sqrt ((x_os_B - x_os_A) ** 2 + (y_os_B - y_os_A) ** 2)) * 100)) / 100)

print ('Дистанция между точками в 2D пространстве =', distance)