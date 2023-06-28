import json


def my_read_json(file_name):
    try:
        with open(file_name, 'r', encoding='UTF-8') as f:
            return [(v['name'], int(k), v['access_level']) for k, v in json.load(f).items()]
    except ValueError:
        print('Ошибка в структуре JSON - файла')
    except FileNotFoundError:
        print('Ошибка. Файл не найден!')
    except:
        print('Неизвестная мне ошибка')
