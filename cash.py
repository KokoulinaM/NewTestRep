def my_decor_cash(dec_foo):
    my_decor_cash.cache = {}

    def wr(*args, **kwargs):
        if kwargs.__len__() != 0:
            b = tuple(sorted(kwargs.values(), key=lambda x: x))
            args = b
            kwargs.clear()
        if my_decor_cash.cache.get(args) is not None:
            result = my_decor_cash.cache[args]
            print("Взяли из кэша")
        else:
            result = dec_foo(*args, **kwargs)
            print("Посчитали заново и поместили в кэш")
            my_decor_cash.cache[args] = result
        return result

    return wr


@my_decor_cash
def foo(b =0, a =0):
    return a*b


print(foo(2, 5))
print(foo(b=5, a=2))
print(foo(2, 5))
print(foo(b=9, a=7))
print(foo(7, 9))
print(foo(a=2, b=5))

'''
import functools as ft
ft.lru_cache
'''