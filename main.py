import json
import os
from jsonschema import validate
import logging


def open_schema():
    """Открываем файл с данными проверки и добавляем в список"""
    list_file = os.listdir(path='schema')
    app_list = []
    for i in list_file:
        with open(f'schema/{i}', 'r', encoding='utf-8') as f:
            text = json.load(f)
            app_list.append(text)
    return app_list


def open_event():
    """Открываем файл с неправильно написанными данными json и добавляем ошибки в файл log"""
    list_file = os.listdir(path='event')

    for i in list_file:
        with open(f'event/{i}', 'r', encoding='utf-8') as f:
            text = json.load(f)
            a = 0
            while a < 4:
                try:
                    validate(text, open_schema()[a])
                except Exception:
                    pass
                    validate(text, open_schema()[a])
                finally:
                    logging.exception("Oops:")
                    a += 1
                    continue


logging.basicConfig(level=logging.DEBUG, filename='myapp.log')


if __name__ == '__main__':
    open_schema()
    open_event()
