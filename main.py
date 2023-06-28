# Погружение в Python (семинары)
# Урок 13. Исключения

import my_utils6 as mu6
import json

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

    my_user = mu6.MyUser('Иван', 1 , 3)
    print(my_user)

    u = mu6.my_read_json('users_base.json')

    print(u)
