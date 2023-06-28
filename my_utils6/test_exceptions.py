"""
Функции для занятия об искключениях
"""

# Задание №1
# - Создайте функцию, которая запрашивает числовые данные от
# пользователя до тех пор, пока он не введёт целое или
# вещественное число.
# - Обрабатывайте не числовые данные как исключения.
def my_get_num() -> float:
    """
    Вводим число с проверкой
    :return:
    """
    ret = 0
    while True:
        try:
            ret = float(input('Введите целое число: '))
            break
        except ValueError:
            print('Ошибка! Введено не целое число!')
    return ret

# Задание №2
# - Создайте функцию аналог get для словаря.
# - Помимо самого словаря функция принимает ключ и значение по умолчанию.
# - При обращении к несуществующему ключу функция должна возвращать дефолтное значение.
# - Реализуйте работу через обработку исключений.
def get_like_dict(my_dict :dict, my_key, default):
    """
    Возвращаем значение словаря по ключу
    :param my_dict: словарь в котором ищем значение по ключу
    :param my_key: Ключ, который ищем
    :param default: Значение, которое возвращаем, если запрашиваемого ключа не находим
    :return:
    """
    pass
