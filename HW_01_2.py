"""
Напишите класс метакласс Meta, который всем классам, для кого он будет метаклассом, устанавливает порядковый номер.
Код для проверки правильности решения:

# class Meta(type):
#     # тут должно быть ваше решение
#
#
# Meta.children_number = 0
#
# class Cls1(metaclass=Meta):
#     def __init__(self, data):
#         self.data = data
#
#
# class Cls2(metaclass=Meta):
#     def __init__(self, data):
#         self.data = data
#
# assert (Cls1.class_number, Cls2.class_number) == (0, 1)
# a, b = Cls1(''), Cls2('')
# assert (a.class_number, b.class_number) == (0, 1)
"""


class Meta(type):
    def __new__(cls, name, base, attrs):
        attrs.update({'class_number': 0})
        return type.__new__(cls, name, base, attrs)


Meta.children_number = 0


class Cls1(metaclass=Meta):
    def __init__(self, data):
        self.data = data


class Cls2(metaclass=Meta):
    def __init__(self, data):
        self.data = data


print(Cls1.class_number)
print(Cls2.class_number)
print(Cls2.class_number)
# assert (Cls1.class_number, Cls2.class_number) == (0, 1)
# a, b = Cls1(''), Cls2('')
# assert (a.class_number, b.class_number) == (0, 1)
