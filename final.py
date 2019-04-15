import random as rend
import re
import logging as lg


def my_decor(dec_foo):
    """
    Если функция принимает хотя бы один параметром со значением my_decor.strTest, то не выполняем
    :param dec_foo:
    :return: результат выполнения функции
    """
    my_decor.strTest = "Тест"

    def wr(*args, **kwargs):
        if any(x == my_decor.strTest for x in args):
            print(f"Вызов функции  {dec_foo.__name__}  с параметром {args}")
        else:
            result = dec_foo(*args, **kwargs)
            return result
    return wr


def check_street(street):
    """
    Функция проверяет корректность названия улиц
    :param street: Название предположительной улицы
    :return: Если прошла проверку, то True
    """
    if re.findall(r'[\W|\d]', street).__len__() > 0:
        lg.basicConfig(filename="finish.log", level=lg.INFO)
        lg.warning(street + " - улица не прошла проверку")
        return False
    else:
        return True


@my_decor
def address_gen(typef: str = '') -> str:
    """
     Функция генерации случайных адресов
    """
    while True:
        rstreet = rend.choice(streets)
        if check_street(rstreet):
            return country + ', ' + city + ', ' + rstreet + ', ' + str(rend.randint(1, 255)) + '-' \
                   + str(rend.randint(1, 2000)) + ' ' + typef
        else:
            break


if __name__ == '__main__':
    country = 'Russia'
    city = 'Spb'
    streets = ('Ordjonikidze', 'Lensoveta//g', 'Nevsky', 'Bogatirsky', 'Novaya-f', 'Cvetochnaya', 'Tipanova')

    for i in range(25):
        print(address_gen(''))

    address_gen('Тест')
