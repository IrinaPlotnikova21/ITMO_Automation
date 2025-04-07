# Задача 1
def task_func (a=(1, 2, 3, 4)):
    return a[1]

print(task_func())

# Задача 2
def compute_surfase(radius, pi=3.14159):
    return pi * radius *radius

print(compute_surfase(2))

#Задача 3
def string_length(s: str = '') -> int:
    return  len(s)

def min_list(a: list, b: list) -> int:
    return max(len(a), len(b))


#Задача 4