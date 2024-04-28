from typing import Union
from accessify import private, protected
import random


class PersonError(Exception):
    """ Вызывается при ненрмальном желании контактировать с несимпатичной персоной"""


class RangeError(Exception):
    """Вызывается при оценке запредельным значением"""


class Person:
    __slots__ = ('name', '_age', '_height', '_cuteness', '_face', '_figure', '_clothes',
                 '_community', '_mind', '_character', '_bad_habits')
    __MIN_AGE = 12
    __MAX_AGE = 80
    __MIN_HEIGHT = 120
    __MAX_HEIGHT = 225
    __MIN_RATING = 0.0
    __MAX_RATING = 10.0

    def __init__(self, age: int, height: int, cuteness: bool):
        self.age = age
        self.height = height
        self.cuteness = cuteness

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        if not self.check_person_attr_type(value, int) or not self.check_person_age(value):
            raise TypeError(f'возраст должен быть целым числом не меньше {self.__MIN_AGE} и не больше {self.__MAX_AGE}')
        self._age = value

    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, value: int) -> None:
        if not self.check_person_attr_type(value, int) or not self.check_person_height(value):
            raise TypeError(
                f'рост должен быть целым числом не меньше {self.__MIN_HEIGHT} и не больше {self.__MAX_HEIGHT}')
        self._height = value

    @property
    def cuteness(self) -> bool:
        return self._cuteness

    @cuteness.setter
    def cuteness(self, cuteness: bool) -> None:
        if not self.check_person_attr_type(cuteness, bool):
            raise TypeError(f'симпатичность должна быть булевым значением')
        self._cuteness = cuteness

    @classmethod
    def check_person_attr_type(cls, attr, type) -> bool:
        return isinstance(attr, type)

    @classmethod
    def check_person_age(cls, age: int) -> bool:
        return cls.__MIN_AGE <= age <= cls.__MAX_AGE

    @classmethod
    def check_person_height(cls, height: int) -> bool:
        return cls.__MIN_HEIGHT <= height <= cls.__MAX_HEIGHT

    @classmethod
    def check_arg_in_range(cls, arg: Union[float, int]) -> bool:
        if isinstance(arg, Union[float, int]) and cls.__MIN_RATING <= arg <= cls.__MAX_RATING:
            return cls.__MIN_RATING <= arg <= cls.__MAX_RATING
        else:
            raise RangeError(f'Оцениваем целыми или десятичными числами от {cls.__MIN_RATING} до {cls.__MAX_RATING}')

    def evaluate_appearance(self, face: Union[float, int], figure: Union[float, int],
                            clothes: Union[float, int]):
        if self.cuteness:
            self._face = face
            self._figure = figure
            self._clothes = clothes

    @property
    def face(self) -> Union[float, int]:
        return self._face

    @face.setter
    def face(self, value: Union[float, int]) -> None:
        self.check_arg_in_range(value)
        self._face = value

    @property
    def figure(self) -> Union[float, int]:
        return self._figure

    @figure.setter
    def rating_face(self, value: Union[float, int]) -> None:
        self.check_arg_in_range(value)
        self._figure = value

    @property
    def clothes(self) -> Union[float, int]:
        return self._clothes

    @clothes.setter
    def clothes(self, value: Union[float, int]) -> None:
        self.check_arg_in_range(value)
        self._clothes = value

    def evaluate_person(self, community: Union[float, int], mind: Union[float, int],
                        character: Union[float, int], bad_habits: bool):
        self._community = community
        self._mind = mind
        self._character = character
        self._bad_habits = bad_habits

    @property
    def community(self) -> Union[float, int]:
        return self._rating_face

    @community.setter
    def community(self, value: Union[float, int]) -> None:
        self.check_arg_in_range(value)
        self._community = value

    @property
    def mind(self) -> Union[float, int]:
        return self._mind

    @mind.setter
    def mind(self, value: Union[float, int]) -> None:
        self.check_arg_in_range(value)
        self._mind = value

    @property
    def character(self) -> Union[float, int]:
        return self._character

    @character.setter
    def character(self, value: Union[float, int]) -> None:
        self.check_arg_in_range(value)
        self._character = value

    def __str__(self):
        return f'{self.__dir__}'


class Man(Person):
    __slots__ = ('_salary', '_confidence')

    def __init__(self, age: int, height: int, cuteness: bool):
        super().__init__(age, height, cuteness)

    @classmethod
    def check_confidence(cls, value):
        if cls.check_arg_in_range(value):
            cls._confidence = value

    @classmethod
    def check_salary(cls, value):
        cls._salary = value

    @property
    def confidence(self):
        return self._confidence

    @confidence.setter
    def confidence(self, value):
        if self.check_arg_in_range(value):
            self._confidence = value

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        if isinstance(salary, int):
            self._salary = salary
        else:
            raise TypeError('Доход указывать в целых числах')


class Girl(Person):
    __slots__ = ('_has_boyfriend', '_job', '_money')

    def __init__(self, age: int, height: int, cuteness: bool):
        super().__init__(age, height, cuteness)

    def check_boyfriend(self, value: bool) -> None:
        if isinstance(value, bool):
            self._has_boyfriend = value

    @property
    def has_boyfriend(self) -> bool:
        return self._has_boyfriend

    @has_boyfriend.setter
    def has_boyfriend(self, value: bool) -> None:
        if isinstance(value, bool):
            self._has_boyfriend = value

    def check_job(self, value: bool) -> None:
        if isinstance(value, bool):
            self._job = value

    @property
    def job(self) -> bool:
        return self._job

    @job.setter
    def job(self, value: bool) -> None:
        if isinstance(value, bool):
            self._job = value

    def check_money(self, value: int) -> None:
        if isinstance(value, int):
            self._money = value

    @property
    def money(self) -> int:
        return self._money

    @money.setter
    def money(self, value: int) -> None:
        if isinstance(value, int):
            self._money = value


class Coush_Test:

    m_age = int(input('Введите свой возраст: '))
    m_height = int(input('Введите свой рост: '))
    m_cuteness = True if input('Считаете ли вы себя привлекаательным (да/нет): ') == 'да' else False
    print('\n')

    print('Теперь перейдем к оценке вашей внешности\n')

    m_face = float(input('Насколько бы вы оценили красоту своего лица: '))
    m_figure = float(input('Насколько бы вы оценили красоту своей фигуры: '))
    m_clothes = float(input('Насколько бы вы оценили свою манеру одеваться: '))
    print('\n')

    print('Отлично, перейдем к вашим духовным качествам!\n')

    m_community = float(input('Насколько вы бы оценили свои умение поддержать разговор: '))
    m_mind = float(input('Насколько вы бы оценили свои интеллектуальные спосбнсти: '))
    m_character = float(input('Насколько вы бы оценили свой характер: '))
    m_bad_habits = True if input('Есть ли у вас вредные привычки (да/нет): ') == 'да' else False
    print('\n')

    print('Стоит также указать еще несклько важных параметров\n')

    m_confidence = float(input('Оцените свою уверенность: '))
    m_salary = int(input('Укажите свой месячный доход: '))
    print('\n')

    man = Man(m_age, m_height, m_cuteness)
    man.evaluate_appearance(m_face, m_figure, m_clothes)
    man.evaluate_person(m_community, m_mind, m_character, m_bad_habits)
    man.check_confidence(m_confidence)
    man.check_salary(m_salary)

    print('Перейдем к оценке девушки\n')

    g_age = int(input('Введите возраст девушки: '))
    g_height = int(input('Введите рост ее рост: '))
    g_cuteness = True if input('Считаете ли вы ее привлекаательной (да/нет): ') == 'да' else False
    print('\n')

    print('Оцените внешность вашей избранницы\n')

    g_face = float(input('Насколько бы вы оценили красоту ее лица: '))
    g_figure = float(input('Насколько бы вы оценили красоту ее фигуры: '))
    g_clothes = float(input('Насколько бы вы оценили ее манеру одеваться: '))
    print('\n')

    flag = True if input('Общались ли вы с этой девушкой (да/нет): \n') == 'да' else False

    if flag:
        g_community = float(input('Насколько вы бы оценили свои умение поддержать разговор: '))
        g_mind = float(input('Насколько вы бы оценили свои интеллектуальные спосбнсти: '))
        g_character = float(input('Насколько вы бы оценили свой характер: '))
        g_bad_habits = True if input('Есть ли у нее вредные привычки (да/нет): ') == 'да' else False
        print('\n')

        print('Стоит также указать еще несклько важных параметров\n')

        g_boyfriend = True if input('Есть ли у нее парень/муж (да/нет): ') == 'да' else False
        g_job = True if input('Работает ли она (да/нет): ') == 'да' else False
        g_money = int(input('Оцените ее финансовые ожидания в месяц: '))


    girl = Girl(g_age, g_height, g_cuteness)
    girl.evaluate_appearance(g_face, g_figure, g_clothes)

    if flag:
        girl.evaluate_person(g_community, g_mind, g_character, g_bad_habits)
        girl.check_boyfriend(g_boyfriend)
        girl.check_job(g_job)
        girl.check_money(g_money)


if __name__ == '__main__':
    test = Coush_Test()
