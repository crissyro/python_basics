from accessify import private, protected



class Girl:
    girl_attr = {}

    def __init__(self, age: int, height: float, weight: float):
        self.girl_attr['age'] = age
        self.girl_attr['height'] = height
        self.girl_attr['weight'] = weight

