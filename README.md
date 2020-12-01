# script_for_Welltory

Сервис по работе 

### Требования


[Python](https://www.python.org/downloads/) v3.7 +  для запуска.
Установите зависимости и виртуальное окружение и запустите скрип.

```sh
$ python main.py

```

Запуск через докер

[Docker](https://www.docker.com/)

Установка для linux
```sh
$ sudo apt update
$ sudo apt install apt-transport-https ca-certificates curl gnupg-agent software-properties-common -y
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
$ sudo add-apt-repository \
$ "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
$ (lsb_release -cs) \
$ stable"
$ sudo apt update
$ sudo apt install docker-ce -y
```

После установки выполнить следующие действия:
1. В корневой директории проекта создайте образ командой docker build -t <тут введите имя образа> .
2. Запустите контейнер командой docker run -it -p 8000:8000 <имя образа>
3. Запустить контейнер снова
4. Командой docker ps узнать container id и через команду docker exec -it <container id> ls можно будет увидить созданые файлы.

### Пример ошибки в файле myapp.log
```sh
jsonschema.exceptions.ValidationError: 'labels' is a required property

Failed validating 'required' in schema:
    {'$schema': 'http://json-schema.org/schema#',
     'properties': {'id': {'type': ['null', 'integer']},
                    'labels': {'items': {'properties': {'category': {'type': ['null',
                                                                              'string']},
                                                        'color': {'type': ['null',
                                                                           'object']},
                                                        'is_custom_tag': {'type': 'boolean'},
                                                        'name_en': {'type': 'string'},
                                                        'name_ru': {'type': 'string'},
                                                        'property_arousal': {'type': ['string',
                                                                                      'null']},
                                                        'property_pleasure': {'type': ['string',
                                                                                       'null']},
                                                        'property_stability': {'type': ['string',
                                                                                        'null']},
                                                        'property_vitality': {'type': ['string',
                                                                                       'null']},
                                                        'property_where': {'type': ['string',
                                                                                    'null']},
                                                        'slug': {'type': 'string'},
                                                        'type': {'type': 'integer'},
                                                        'type_stress': {'type': 'integer'}},
                                         'required': ['category',
                                                      'color',
                                                      'is_custom_tag',
                                                      'name_en',
                                                      'name_ru',
                                                      'property_arousal',
                                                      'property_pleasure',
                                                      'property_stability',
                                                      'property_vitality',
                                                      'property_where',
                                                      'slug',
                                                      'type',
                                                      'type_stress'],
                                         'type': 'object'},
                               'type': 'array'},
                    'rr_id': {'type': ['null', 'integer']},
                    'timestamp': {'type': 'string'},
                    'unique_id': {'type': 'string'},
                    'user': {'properties': {'id': {'type': 'integer'}},
                             'required': ['id'],
                             'type': 'object'},
                    'user_id': {'type': 'integer'}},
     'required': ['id',
                  'labels',
                  'rr_id',
                  'timestamp',
                  'unique_id',
                  'user',
                  'user_id'],
     'type': 'object'}

On instance:
    {'created_at': '2020-09-07T12:06:02.833131Z',
     'data': {'case_id': 1,
              'cmarkers': [],
              'datetime': '2020-07-23T11:41:00.230098',
              'group': 1,
              'id': 321111,
              'ignore_duplicates': True,
              'qa_hash': '243302096055315412925961701989226483309',
              'show_case_id': True,
              'source': 'TriggerExample',
              'time_of_day': 'morning',
              'timestamp': '2020-09-07T14:36:02.685109',
              'user': {'is_android_user': True,
                       'is_aw_user': True,
                       'is_ios_user': True,
                       'is_old_user': True,
                       'is_web_user': True,
                       'segments': [{'id': 4, 'slug': 'paid'}]},
              'user_id': 155288},
     'environment_id': 2,
     'event': 'cmarker_created',
     'id': '3b4088ef-7521-4114-ac56-57c68632d431',
     'user_id': 123}

```


## Авторы

* **Vladimir Svetlakov** - [svvladimir-ru](https://github.com/svvladimir-ru)