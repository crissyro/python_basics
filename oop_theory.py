# инициализатор и финилизатор

class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        print(f'Deleting {self}')

    #имитация запрета обращения к атрибуту x
    def __getattribute__(self, item):
        if item == 'x':
            raise AttributeError
        else:
            print('Active magic magic method __getattribute__')
            return object.__getattribute__(self, item)

    #запрет на использования имени атрибута
    def __setattr__(self, key, value):
        if key == 'z':
            raise AttributeError
        else:
            print('Active magic magic method __setattr__')
            object.__setattr__(self, key, value)

    # автоматически вызывается при обращение к несуществующему атрибуту
    # без него вылезает ошибка
    def __getattr__(self, item):
        print(f"Active magic magic method __getattr__ + {item}")

    # удаляет локальное свойство с помощью ф-ции del
    def __delattr__(self, item):
        print(f"Active magic magic method __delattr__ + {item}")
        object.__delattr__(self, item)


#метод __new__ что то типо singleton

class Database:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __del__(self):
        Database.__instance = None

    def __init__(self, user, port):
        self.user = user
        self.port = port

    def close(self):
        print('Closing')

    def read(self):
        return "Data"


# использовать декоратор @classmethod  для функций внутренних проверок,
# иначе есть @staticmethod без скрытых аргументов


#   механизмы инкапсуляции
#   atr -  public
#   _atr - protected (для обращения внутри класса и в дочерних)
#   __atr - private  (обращение только внутри класса

# from accessify import private, protected


# реализация паттерна моносостояние

class ThreadData:
    __shared_attrs = {
        'name': 'thred1',
        'data': {},
        'id': 1
    }

    def __init__(self):
        self.__dict__ = self.__shared_attrs


# дескриптор

class Integer:

    @classmethod
    def is_int(cls, value):
        if type(value) != int:
            raise TypeError

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.is_int(value)
        setattr(instance, self.name, value)


class Point:

    x = Integer()
    y = Integer()
    z = Integer()

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

