# Задача 1
num_float = -3.4

# Так же попробуйте следующие варианты
# num_float  = 0
# num_float  = -4.5

if num_float > 0:
    print('положительное число')
elif num_float == 0:
    print('ноль')
else:
    print('число отрицательное')


# Задача 2
num = 3
permit_print = True

if num > 0 and permit_print:
    print('num - положительное число')
elif not permit_print:
    print('печать запрещена')


# Задача 3
def student_rank(year_of_study):
    if year_of_study == 2 or year_of_study ==3 or year_of_study == 4:
        print("Бакалавр")
    elif year_of_study in range(5, 7):
        print("Магистр")
    elif 7 <= year_of_study <=9:
        print("Аспирант")
    else:
        print("Введите корректный код обучения")

student_rank(8)

# Задача 4

a = -200

if a > 100 or a < -100:
    print('-')
else:
    print('+')