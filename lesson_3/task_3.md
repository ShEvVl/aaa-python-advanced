# Задачи по декораторам

## Задача №1

Для начала, давайте подменим метод `write` у объекта `sys.stdin` на такую функцию, которая перед каждым вызовом оригинальной функции записи данных в `stdout` допечатывает к тексту текущую метку времени.

```python
original_write = sys.stdout.write

def my_write(string_text):
    pass # Write your own code

sys.stdout.write = my_write
print('1, 2, 3')

>>> [2021-12-05 12:00:00]: 1, 2, 3

sys.stdout.write = original_write
```

## Задача №2

Упакуйте только что написанный код в декторатор. Весь вывод фукнции должен быть помечен временными метками так, как видно выше.

```python
def timed_output(function):
    pass # TODO: Write your code.

@timed_output
def print_greeting(name):
    print(f'Hello, {name}!')

print_greeting("Nikita")

>>> [2021-12-05 12:00:00]: Hello, Nikita!
```

## Задача №3

Напишите декторатор, который будет перенаправлять вывод фукнции в файл.

>Подсказка: вы можете заменить объект sys.stdout каким-нибудь другим объектом.

```python
def redirect_output(filepath):
    pass # TODO: Write everything printed to stdout

@redirect_output('./function_output.txt')
def calculate():
    for power in range(1, 5):
        for num in range(1, 20):
            print(num ** power, end=' ')
        print()

calculate()
%cat function_output.txt

>>> 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
1 4 9 16 25 36 49 64 81 100 121 144 169 196 225 256 289 324 361
1 8 27 64 125 216 343 512 729 1000 1331 1728 2197 2744 3375 4096 4913 5832 6859
1 16 81 256 625 1296 2401 4096 6561 10000 14641 20736 28561 38416 50625 65536 83521 104976 130321
```
