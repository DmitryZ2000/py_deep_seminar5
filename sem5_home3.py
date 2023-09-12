# Создайте функцию генератор чисел Фибоначчи

def fibonacci(num):
    '''Функция-генератор чисел Фибоначи'''
    a, b = 1, 1
    yield a
    if num == 2:
        yield b
    if num > 2:
        for _ in range(3, num + 2):
            b, a = a + b , b
            yield b


n = 20
for i in fibonacci(n):
    print(i, end='  ')