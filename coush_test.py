import random
import typing
from accessify import private, protected
import math


class Girl:
    __MAX_HEIGHT = 1.95
    __MAX_WEIGHT = 80
    __MAX_AGE = 50

    def __init__(self, age: int, height: float, weight: float):
        self.age = age
        self.height = height
        self.weight = weight

    @classmethod
    def check_adecvatnost(self)->int:
        res_check_adecvatnost = 0

        if self.height > self.__MAX_HEIGHT:
            print(f"Рост {self.height} - ты пьяный?")
            res_check_adecvatnost = -50

        if self.weight > self.__MAX_WEIGHT:
            print(f"Вес {self.weight}-ты пьяный?")
            res_check_adecvatnost = -50


        if self.age > self.__MAX_AGE:
            print(f"Возраст {self.age}-ты пьяный?")
            res_check_adecvatnost = -50

        return res_check_adecvatnost

    @classmethod
    def check_negative_attr(self):
        list_neg_attr = list(input().split())
        return list_neg_attr

    @classmethod
    def check_beauty(self, face: float, fashion: float, figure: float)->float:
        return face * fashion * figure / 3

    @classmethod
    def check_positive_attr(self)->list:
        list_pos_attr = list(input().split())
        return list_pos_attr

