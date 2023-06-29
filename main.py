# Погружение в Python (семинары)
# Урок 13. Исключения

import my_utils6 as mu6

if __name__ == '__main__':
    print('--== Тестирование числовой функции ==--')
    print(f'Вы ввели число {mu6.my_get_num()}')

    print('\n--== Тестирование функции get как у словаря ==--')
    my_dict = {1: 'One',
               'key1': 'String key!',
               32: 32,
               'key6': 'Top secret',
               }
    print(mu6.get_like_dict(my_dict, 'key1', 'default1'))
    print(mu6.get_like_dict(my_dict, 32, 'default_32'))
    print(mu6.get_like_dict(my_dict, 43, 'default_43'))  # Тут отработает исключение

    print('\n--== Тестирование класса MyUser и коллекции из этого класса ==--')
    my_user1 = mu6.MyUser('Anna', 2, 3)
    print(my_user1)

    user_list = [mu6.MyUser(i_user, i_id, i_level)
                 for i_user, i_id, i_level in mu6.my_read_json('users_base.json')]
    print('Список пользователей с ID И уровнем доступа:')
    print(*user_list, sep='\n')

    print('\n--== Тестирование класса MyAccess ==--')
    print('Тестируем метод login:')
    my_access = mu6.MyAccess('users_base.json')
    try:
        my_access.login(my_user1)
        print(f'Пользователю {my_access.logged_user.name} предоставлен доступ '
              f'с уровнем {my_access.logged_user.access_level}')
    except mu6.MyAccessException as e:
        print(e)

    my_user2 = mu6.MyUser('Peter', 2, 2)
    try:
        my_access.login(my_user2)
        print(f'Пользователю {my_access.logged_user.name} предоставлен доступ '
              f'с уровнем {my_access.logged_user.access_level}')
    except mu6.MyAccessException as e:
        print(e)

    print('Тестируем метод add')
    my_user4 = mu6.MyUser('Viktor', -1, 5)
    try:
        my_access.add_user(my_user4)
        print(f'Пользователь {my_user4} успешно добавлен в список доступа!')
    except mu6.MyLevelException as e:
        print(e)

    my_user5 = mu6.MyUser('Maria', -1, 1)
    try:
        my_access.add_user(my_user5)
        print(f'Пользователь {my_user5} успешно добавлен в список доступа!')
    except mu6.MyLevelException as e:
        print(e)

    print('Список пользователей с ID И уровнем доступа:')
    my_access.print_users()

    print('\n--== ДОМАШНЕЕ ЗАДАНИЕ!!!! ==--')
    print('--== Тестирование класса MyRectangle ==--')
    rec1 = mu6.MyRectangle(3, 4)
    rec2 = mu6.MyRectangle(30.5, 40)
    rec3 = mu6.MyRectangle(1)
    print(rec1)
    print(rec2)
    try:
        rec3 = rec1 - rec2
    except mu6.MyValueError as e:
        print(e)
    print(rec3)

    try:
        rec3 = rec2 - rec1
    except mu6.MyValueError as e:
        print(e)
    print(rec3)

    print('--== Тестирование класса MyFactorial ==--')
    try:
        f1 = mu6.MyFactorial(7)
    except mu6.MyValueError as e:
        print(e)
    else:
        print(f1)

    try:
        f2 = mu6.MyFactorial(-7)
    except mu6.MyValueError as e:
        print(e)
    else:
        print(f2)

# Результат работы:
# C:\Work\python\dz3\Py3HW13\venv\Scripts\python.exe C:/Work/python/dz3/Py3HW13/main.py
# --== Тестирование числовой функции ==--
# Введите целое число: a
# Ошибка! Введено не целое число!
# Введите целое число: -3.3
# Ошибка! Введено не целое число!
# Введите целое число: -5
# Вы ввели число -5
#
# --== Тестирование функции get как у словаря ==--
# String key!
# 32
# default_43
#
# --== Тестирование класса MyUser и коллекции из этого класса ==--
# Имя: Anna, ID:2, Уровень доступа:3
# Список пользователей с ID И уровнем доступа:
# Имя: Ivan, ID:1, Уровень доступа:3
# Имя: Peter, ID:2, Уровень доступа:2
# Имя: Anna, ID:3, Уровень доступа:1
#
# --== Тестирование класса MyAccess ==--
# Тестируем метод login:
# MyAccessException, Доступ запрещен! Пользователя Anna с ID 2 не существует!
# Пользователю Peter предоставлен доступ с уровнем 2
# Тестируем метод add
# MyLevelException, Добавление невозможно! Недостаточный уровень доступа!
# Пользователь Имя: Maria, ID:4, Уровень доступа:1 успешно добавлен в список доступа!
# Список пользователей с ID И уровнем доступа:
# Имя: Ivan, ID:1, Уровень доступа:3
# Имя: Peter, ID:2, Уровень доступа:2
# Имя: Anna, ID:3, Уровень доступа:1
# Имя: Maria, ID:4, Уровень доступа:1
#
# --== ДОМАШНЕЕ ЗАДАНИЕ!!!! ==--
# --== Тестирование класса MyRectangle ==--
# Прямоугольник 3 x 4
# Прямоугольник 30.5 x 40
# MyValueError, Значение -27.5 должно быть больше 0
# Прямоугольник 1 x 1
# Прямоугольник 27.5 x 36
# --== Тестирование класса MyFactorial ==--
# 5040
# MyValueError, Факториал от отрицательного числа не считаем!
#
# Process finished with exit code 0
