import datetime as dt
import  time


def my_decor_cash(dec_foo):
    my_decor_cash.cache = {}

    def wr(*args, **kwargs):
        if kwargs.__len__() != 0:
            b = tuple(sorted(kwargs.values(), key=lambda x: x))
            args = b
            kwargs.clear()
        if my_decor_cash.cache.get(args) is not None:
            result = my_decor_cash.cache[args]
           # print("Взяли из кэша")
        else:
            result = dec_foo(*args, **kwargs)
           # print("Посчитали заново и поместили в кэш")
            my_decor_cash.cache[args] = result
        return result

    return wr


def my_decor_long(dec_foo):
    def wr(*args, **kwargs):
        dt_start= time.time_ns()
        result=dec_foo(*args, **kwargs)
        print("Время выполнения " + str(time.time_ns() - dt_start))
        return result
    return wr

@my_decor_cash
def fib(x):
   if x==1 or x==0:
       return 1
   else:
       return fib(x-1)+fib(x-2)


def fib_(x):
   if x==1 or x==0:
       return 1
   else:
       return fib(x-1)+fib(x-2)
'''
x=fib()
for i in range(31):
    a=next(x)
'''
timedecor=my_decor_long(lambda x:fib(x))
print(timedecor(100))
print(timedecor(300))
#print(timedecor(50))
timedecor_=my_decor_long(lambda x:fib_(x))
print("без кэша")
print(timedecor_(100))
print(timedecor_(300))
#print(timedecor_(50))

