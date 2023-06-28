# Задание №4
# - Вспоминаем задачу из семинара 8 про сериализацию данных, где в бесконечном цикле запрашивали имя,
# личный идентификатор и уровень доступа (от 1 до 7) сохраняя информацию в JSON файл.
# - Напишите класс пользователя, который хранит эти данные в свойствах экземпляра.
# - Отдельно напишите функцию, которая считывает информацию из JSON файла и
# формирует множество пользователей.

class MyUser:
    """
    Класс пользователя. Храним его имя, ID и уровень доступа
    """
    def __init__(self, name, my_id: int, access_level: int):
        self.name = name
        self.id = my_id
        self.access_level = access_level

    def __str__(self):
        return f'Имя: {self.name}, ID:{self.id}, Уровень доступа:{self.access_level}'

    def __eq__(self, other):
        return self.name == other.name and self.id == other.id
