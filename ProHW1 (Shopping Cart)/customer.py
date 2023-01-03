# class that describes the customers

class Customer:
    def __init__(self, name: str, surname: str, phone_number: int):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number

    def __str__(self):
        return f'{self.name} {self.surname}\nphone: {self.phone_number}'