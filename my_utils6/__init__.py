"""
Init-файл для пакета с моими классами для 11-ого домашнего задания
"""
from my_utils6.test_exceptions import my_get_num
from my_utils6.test_exceptions import get_like_dict
from my_utils6.MyUser import MyUser
from my_utils6.utils import my_read_json

# Эти классы будем "экспортировать" для внешней работы
__all__ = ['my_get_num', 'get_like_dict', 'MyUser', 'my_read_json']
