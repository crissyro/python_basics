import random
import typing
from accessify import private, protected
import math


class Girl:
    girl_attr = {}

    __MAX_HEIGHT = int(input('input your max height: '))
    __MAX_WEIGHT = int(input('input your max weight: '))
    __MAX_AGE = int(input('input your max age: '))

    def __init__(self, age: int, height: float, weight: float):
        self.girl_attr['age'] = age
        self.girl_attr['height'] = height
        self.girl_attr['weight'] = weight

    @classmethod
    def check_normal(self)->int:
        res_check_normal = 0

        if self.girl_attr['height'] > self.__MAX_HEIGHT:
            print(f' {self.girl_attr["height"]} is too big')
            res_check_normal = -50

        if self.girl_attr['weight'] > self.__MAX_WEIGHT:
            print(f'{self.girl_attr["weight"]} is too big')
            res_check_normal = -50

        if self.girl_attr['age'] > self.__MAX_AGE:
            print(f'{self.girl_attr["age"]} is too big')
            res_check_normal = -50

        return res_check_normal

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

