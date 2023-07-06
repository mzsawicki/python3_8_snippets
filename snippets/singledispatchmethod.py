from functools import singledispatchmethod


class WeakTypedString:
    def __init__(self, initial_value: str):
        self._string = initial_value

    def __str__(self):
        return self._string

    @singledispatchmethod
    def concat(self, value):
        self._string += value

    @concat.register(list)
    def _(self, value):
        list_values_string = ' '.join(value)
        self._string += list_values_string

    @concat.register(int)
    def _(self, value):
        self._string += str(value)


weak_string = WeakTypedString('Lorem')
list_ = ['ipsum', 'sir', 'dolor', 'amet']
number = 22

weak_string.concat(' ')
weak_string.concat(list_)
weak_string.concat(' ')
weak_string.concat(number)

print(weak_string)
