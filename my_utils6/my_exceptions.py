# Задание №3
# - Создайте класс с базовым исключением и дочерние классы-исключения:
#  - ошибка уровня,
#  - ошибка доступа.

class MyBaseException(BaseException):
    """
    Базовый класс для работы с моими персональными исключениями
    """
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'MyBaseException, {self.message}'
        else:
            return 'MyBaseException has been raised!'


class MyLevelException(MyBaseException):
    """
    Мой класс для обработки исключений ошибок уровня
    """
    def __init__(self, *args):
        super().__init__(*args)


class MyAccessException(MyBaseException):
    """
    Мой класс для обработки исключений ошибок по доступу
    """
    def __init__(self, *args):
        super().__init__(*args)
