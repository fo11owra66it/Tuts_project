# task 01
# Создать словарь

test_dictionary = {
    "city": "Москва", 
    "temperature": "20"}

print(test_dictionary["city"])    # Вывод на экран значение ключа "city"

test_dictionary["temperature"] = int(test_dictionary["temperature"]) - 5    # Уменьшить значение "temperature" на 5

print(test_dictionary)    # Вывод на экран всего словаря

print(test_dictionary.get("country"))    # Проверка, есть ли в словаре ключ "country"

print(test_dictionary.get("country", "Россия"))    # Вывести значение по-умолчанию "Россия" для ключа country

test_dictionary["date"] = "27.05.2019"    # Добавить в словарь элемент date со значением "27.05.2019"

print(len(test_dictionary))    # Вывести на экран длину словаря