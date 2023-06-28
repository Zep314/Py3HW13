# Задание No5
# Доработаем задачи 3 и 4. Создайте класс проекта, который имеет следующие методы:
# - загрузка данных (функция из задания 4)
# - вход в систему - требует указать имя и id пользователя. Для проверки наличия пользователя
# в множестве используйте магический метод проверки на равенство пользователей. Если такого
# пользователя нет, вызывайте исключение доступа. А если пользователь есть, получите его уровень из
# множества пользователей.
# - добавление пользователя. Если уровень пользователя меньше, чем ваш уровень, вызывайте
# исключение уровня доступа.

from my_utils6.MyUser import MyUser
from my_utils6.utils import my_read_json
from my_utils6.my_exceptions import MyAccessException
from my_utils6.my_exceptions import MyLevelException


class MyAccess:
    """
    Класс - список доступа с возможностью авторизации и добавления нового пользователя в список доступа
    с проверкой
    """
    user_list = []
    logged_user = None

    def __init__(self, file_name='users_base.json'):
        self.file_name = file_name
        self.load_user_list()

    def load_user_list(self):
        """
        Грузим список доступа из JSON-файла
        :return:
        """
        self.user_list = [MyUser(i_user, i_id, i_level)
                          for i_user, i_id, i_level in my_read_json(self.file_name)]

    def login(self, user: MyUser):
        """
        Метод авторизации пользователя
        :param user:
        :return:
        """
        for u in self.user_list:
            if u == user:
                self.logged_user = user
                return u.access_level
        raise MyAccessException(f'Доступ запрещен! Пользователя {user.name} с ID {user.id} не существует!')

    def add_user(self, user: MyUser):
        """
        Метод добавления пользователя
        :param user:
        :return:
        """
        if self.logged_user:
            if user.access_level < self.logged_user.access_level:
                # Вычисляем свободное ID для нового пользователя
                user.id = max([u.id for u in self.user_list], default=0) + 1
                self.user_list.append(user)
            else:
                raise MyLevelException('Добавление невозможно! Недостаточный уровень доступа!')
        else:
            raise MyLevelException('Добавление невозможно! Необходимо авторизоваться!')

    def print_users(self):
        """
        Вывод на печать списка пользователей
        :return:
        """
        for user in self.user_list:
            print(user)
