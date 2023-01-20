# Реализуйте метакласс, который обладает следующим функционалом:
# при его использовании в файл с заранее определенным названием
# нужно сохранить имя класса и список его полей.

class MetaMeta(type):

    def __new__(typeclass, class_name, supers, class_dict):
        return type.__new__(typeclass, class_name, supers, class_dict)

    def __init__(self, class_name, supers, class_dict):
        with open('Metaclass_file', 'w') as f:
            f.write(f'{class_name}:''\n')
            for i in class_dict:
                f.write(i)


class FromMeta(metaclass=MetaMeta):

    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        return self.a + other.a


a = FromMeta(1)
b = FromMeta(2)
print(a+b)
