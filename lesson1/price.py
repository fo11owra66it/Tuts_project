# task 01
# Создать в редакторе файл price.py
# Создать функцию format_price, которая принимает один аргумент price
# Приведите price к целому числу (тип int)
# Верните строку "Цена: ЧИСЛО руб."
# Вызовите функцию, передав на вход 56.24 и положите результат в переменную
# Выведите значение переменной с результатом на экран
def format_price(price: int) -> int:
    return f'Цена: {int(price)} руб.'

total_price = format_price(56.24)

print(total_price)