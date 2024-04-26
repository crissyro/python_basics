from accessify import private, protected


MIN_AGE = 12
MAX_AGE = 80
MIN_HEIGHT = 120
MAX_HEIGHT = 225

class Person:

    def check_person_attr(self, age: int, height:int)->bool:
        return True if MIN_AGE <= age <= MAX_AGE and MIN_HEIGHT <= height <= MAX_AGE else False

    def __init__(self, age: int, height: int, cuteness: bool):
        if self.check_person_attr(self, age, height):
            if type(age) == int and type(height) == int and type(cuteness) == bool:
                 self.attributes = {'age': age, 'height': height, 'cuteness': cuteness}
            else:
                 raise TypeError(f'age and height must be integers, cuteness must be bool')




    def __str__(self):
        print(f'{self.attributes}')





class Man(Person):
    def __init__(self, age: int, height: int, cuteness: bool):
        super().__init__(self, age, height, cuteness)



