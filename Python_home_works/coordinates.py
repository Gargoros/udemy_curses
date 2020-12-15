#Запросить у пользователя координаты x и y двух точек на плоскости.
#Посчитать расстояние между заданными точками
#и вывести результат на консоль с точностью до трёх знаков после запятой
#(плавающей точки).
import math

print("To calculate the distance between two points, enter their coordinates ")

print("Enter two coordinates of a point separated by a space ")
point_x1, point_y1 = (input("Enter the coordinates of the first point ").split())
point_x2, point_y2 = (input("Enter the coordinates of the second point ").split())

x1, y1 = float(point_x1), float(point_y1)
x2, y2 = float(point_x2), float(point_y2)

distance = math.sqrt((x2 - x1)** 2 + (y2 - y1)** 2)
print(round(distance, 3))