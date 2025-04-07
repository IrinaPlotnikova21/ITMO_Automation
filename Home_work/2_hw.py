#Задача 1
def task_1 () -> None:
    a: int = 2
    b: float = 3.14
    c: str = 'Hi'
    d: list = [1, 2, 3]
    e: bool = True
    print(type(a))
    print(type(b))
    print(type(c))
    print(type(d))
    print(type(e))

task_1()


#Задача 2
def task_2 () -> None:
    int_tuple: tuple = (1, 2, 3, 5, 8, 13, 21)
    print(int_tuple[0:3])

task_2()


#Задача 3
def task_3 (number: int) -> int:
    return number**2

print(task_3(5))