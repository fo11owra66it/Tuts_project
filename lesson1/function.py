# task 01
# Создаnь функцию get_summ(one, two, delimiter='&'),
# которая принимает два параметра, приводит их к строке
# и отдает объединенными через разделитель delimiter
# Вызвать функцию, передав в нее два аргумента "Learn" и "python",
# положить результат в переменную и выведите ее значение на экран
# Сделайте так, чтобы результирующая строка выводилась заглавными буквами
def get_summ(one: str, two: str, delimiter='&') -> str:
    return one + delimiter + two

str_summ = get_summ("Learn", "python")

print(str_summ.upper())
