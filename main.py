# Погружение в Python (семинары)
# Урок 13. Исключения

import my_utils6 as mu6

if __name__ == '__main__':
    print('--== Тестирование числовой функции ==--')
    #    print(f'Вы ввели число {mu6.my_get_num()}')

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
    # for i_user, i_id, i_level in mu6.my_read_json('users_base.json'):
    #     user_list.append(mu6.MyUser(i_user, i_id , i_level))
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
    print('--== Тестирование класса ????? ==--')
