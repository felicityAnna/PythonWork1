# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

quarter  = int(input("Введите четверть: "))

if (quarter == 1) :
    print ('Координаты в 1й четверти: X от 0 до +∞, Y от 0 до +∞')
elif (quarter == 2) :
    print ('Координаты во 2й четверти: X от 0 до -∞, Y от 0 до +∞')
elif (quarter == 3) :
    print ('Координаты в 3й четверти: X от 0 до -∞, Y от 0 до -∞')
elif (quarter == 4)  :
    print ('Координаты в 4й четверти: X от 0 до +∞, Y от 0 до -∞')
else : 
    print ('Такой четверти не существует, введите число от 1 до 4')