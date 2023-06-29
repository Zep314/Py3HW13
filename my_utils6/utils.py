"""
Модуль для различных утилит
"""

import json


def my_read_json(file_name):
    """
    Класс-утилита для чтения информации из JSON-файла с обработкой ошибок
    :param file_name:
    :return:
    """
    try:
        with open(file_name, 'r', encoding='UTF-8') as f:
            return [(v['name'], int(k), v['access_level']) for k, v in json.load(f).items()]
    except ValueError:
        print('Ошибка в структуре JSON - файла')
    except FileNotFoundError:
        print('Ошибка. Файл не найден!')
    except BaseException as e:
        print(f'Неизвестная мне ошибка, {e}')
