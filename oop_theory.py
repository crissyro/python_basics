# инициализатор и финилизатор
# from accessify import private, protected



class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        print(f'Deleting {self}')


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

