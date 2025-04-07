# Задача 1
def task_1(a:int, b:int) -> None:
    if a > b:
        print(a)
    elif b > a:
        print(b)

task_1(2, 3)


# Задача 2
def task_2(a:int, b:int) -> None:
    if a - b == 135 or b - a == 135:
        print('Yes')
    else:
        print('No')

task_2(100, 235)
task_2(200, 400)
task_2(335, 200)


# Задача 3
def task_3(month:int) -> None:
    if month == 12 or month == 1 or month == 2:
        print('Зима')
    elif month in range (3, 6):
        print('весна')
    elif month in range (6, 9):
        print('лето')
    elif month in range (9, 12):
        print('осень')
    else:
        print('Error')

task_3(1)
task_3(12)
task_3(9)
task_3(15)


# Задача 4
def task_4(a:int, b:int, c:int) -> None:
    if a > 10 and b > 10 and c > 10:
        print('Yes')
    else:
        print('No')

task_4(11, 14, 9)
task_4(11, 12, 13)
task_4(4, 2, 3)


# Задача 5
def task_5(number_list:list) -> int:
    count = 0

    for number in number_list:
        if number > 0:
            count = count + 1
    return count

print(task_5([1, 2, -3, -4, -5]))


# Задача 6
def task_6(years:int, months:int) -> int:
    return (years * 12 + months) * 29

print(task_6(1, 1))

