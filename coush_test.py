from accessify import private, protected


class Person:
    def __init__(self, age: int, height: int, cuteness: bool):
        self.attributes = {'age': age, 'height': height, 'cuteness': cuteness}





class Man(Person):
    def __init__(self, age: int, height: int, cuteness: bool):
        super().__init__(self, age, height, cuteness)



