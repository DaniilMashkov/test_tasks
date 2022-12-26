import re


# 1
def to_camel_case(text: str) -> str:
    return re.split('_|-', text)[0] + ''.join([word.title() for word in re.split('_|-', text)][1:])


# 2
class SingletonMeta(type):
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__new__(cls, *args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Foo(metaclass=SingletonMeta):
    pass


# 3
count_bits = lambda n: bin(n).count('1')


# 4
def digital_root(n: int) -> int:
    return n if n < 10 else digital_root(sum(map(int, str(n))))


# 5
even_or_odd = lambda number: "Even" if number % 2 == 0 else "Odd"

assert (to_camel_case('abra_ca-da_bra') == 'abraCaDaBra')
assert (id(Foo()) == id(Foo()))
assert (count_bits(14519) == 9)
assert (digital_root(493193) == 2)
assert (even_or_odd(3) == 'Odd')
