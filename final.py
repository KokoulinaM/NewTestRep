import random as rend
import re
import logging as lg
import json

streets = []
lg.basicConfig(filename="finish.log", level=lg.INFO)

with open('streets.txt', 'rt') as f:
    data = f.read()


try:
    streets = json.loads(data)["Streets"]
except json.JSONDecodeError as e:
    pass


def decor(strTest):

    def my_decor(dec_foo):
        """
        Если функция принимает хотя бы один параметром со значением my_decor.strTest, то не выполняем
        :param dec_foo:
        :return: результат выполнения функции
        """

        def wr(*args, **kwargs):
            if strTest in args or strTest in kwargs.values():
                print(f"Вызов функции  {dec_foo.__name__}  с параметром {args}")
            else:
                result = dec_foo(*args, **kwargs)
                return result
        return wr
    return my_decor


def check_street():
    """
    Функция проверяет корректность названия улиц

    """
    for street in streets:
        if re.findall(r'[\W|\d]', street):
            lg.warning(street + " - улица не прошла проверку")
            streets.remove(street)


@decor("Test")
def address_gen(typef=''):
    """
     Функция генерации случайных адресов
    """
    while True:
        rstreet = rend.choice(streets)
        yield country + ', ' + city + ', ' + rstreet + ', ' + str(rend.randint(1, 255)) + rend.choice(lit) +\
            '-' + str(rend.randint(1, 2000)) + ' ' + typef


if __name__ == '__main__':
    country = 'Russia'
    city = 'Spb'
    lit = ('', 'a')
    check_street()

    adr = address_gen()
    for i in range(25):
        print(next(adr))

address_gen("Test")

# json input data
# streets check once
# decorator
