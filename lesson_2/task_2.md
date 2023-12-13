# Самое необходимое о классах 2 (практика)

## Задание #1: вывод цвета

Создайте класс `Color`, который выводит $\color{red}{●}$ в заданном цвете `RGB`

```python
red = Color(255, 0, 0)
print(red)
# Out: ●
```

Выводить в консоль `●` в цвете $\color{red}{R} \color{green}{G} \color{blue}{B}$ можно так

```python
END = '\033[0'
START = '\033[1;38;2'
MOD = 'm'

# Cornflower blue
red_level = 100
green_level = 149
blue_level = 237
print(f'{START};{red_level};{green_level};{blue_level}{MOD}●{END}{MOD}')
# Out: ●
```

## Задание #2: сравнение цветов

Реализуйте возможность сравнивать цвета

```python
red = Color(255, 0, 0)
green = Color(0, 255, 0)
red == green
# Out: False

red == Color(255, 0, 0)
# Out: True
```

## Задание #3: смешивание цветов

Реализуйте смешивание цветов через сложение экземпляров класса `Color`

```python
red = Color(255, 0, 0)
green = Color(0, 255, 0)
red + green
# Out: ●
```

## Задание #4: уникальные цвета

Из списка цветов оставьте только уникальные

```python
orange1 = Color(255, 165, 0)
red = Color(255, 0, 0)
green = Color(0, 255, 0)
orange2 = Color(255, 165, 0)
color_list = [orange1, red, green, orange2]
set(color_list)
# Out: {●, ●, ●}
```

## Задание #5: уменьшение контраста

Реализуйте уменьшение контраста умножением на `с = [0, 1]` экземпляра
класса `Color`

```python
red = Color(255, 0, 0)
# Out: ●

0.5 * red
# Out: ●
```

Желаемая доля контраста

$$c = [0, 1]$$

Уровень контраста

$$cl = -256 \cdot (1-c)$$

Коэффициент коррекции контраста

$$F = \frac{259 \cdot (cl + 255)}{255 \cdot (259 - cl)}$$

Уровень цвета

$$L = [0, 255]$$

Color($\color{red}{L}$, $\color{lightgreen}{L}$, $\color{lightblue}{L}$)

Уровень цвета с измененной контрастностью

$$L' = F \cdot (L - 128) + 128$$

Приблизительная формула для изменения яркости

$$c = [0, 1]$$
$$L = [0, 255]$$
$$cl = -256 \cdot (1-c)$$
$$F = \frac{259 \cdot (cl + 255)}{255 \cdot (259 - cl)}$$
$$L' = F \cdot (L - 128) + 128$$
