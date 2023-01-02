# 1. Створіть клас для опису товару. У якості атрибутів товару можете використовувати значення ціни товару,
# опису товару, габарити товару. Створіть пару екземплярів вашого класу та протестуйте їхню роботу.

class ShopItems:
    def __init__(self, fruit: str, price: float, description: str):
        self.price = price
        self.description = description
        self.fruit = fruit

    def __str__(self):
        return f'{self.fruit}\nkind: {self.description}\nprice: {self.price}'


apple = ShopItems('apple', 40, 'red')
orange = ShopItems('orange', 80, 'Brazil')
banana = ShopItems('banana', 60, 'Thailand')

# 2. Створіть клас "Покупець". У якості атрибутів можна використовувати прізвище,
# ім'я, по батькові, мобільний телефон тощо.


class Customer:
    def __init__(self, name: str, surname: str, phone_number: int):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number

    def __str__(self):
        return f'{self.name} {self.surname}\nphone: {self.phone_number}'


customer1 = Customer('Petro', 'Poroshenko', 380501234567)
customer2 = Customer('Volodymyr', 'Zelenskiy', 380675678912)
customer3 = Customer('Victor', 'Yushchenko', 380985673456)

# 3. Створіть клас "Замовлення". Замовлення може містити декілька товарів певної кількості.
# Замовлення має містити дані про користувача, який його здійснив.
# Реалізуйте метод обчислення сумарної вартості замовлення.
# Визначте метод str() для коректного виведення інформації про це замовлення.


class Order:
    def __init__(self, customer: Customer):
        self.customer = customer
        self.cart_item = []
        self.cart_item_quantity = []

    def add_to_cart(self, product: ShopItems, quantity: float):
        if product in self.cart_item:
            self.cart_item_quantity[self.cart_item.index(product)] += quantity
        else:
            self.cart_item.append(product)
            self.cart_item_quantity.append(quantity)

    def total_price(self):
        total = 0
        for i, item in self.cart_item:
            total += item.price * self.cart_item[i]
        return total

    def __str__(self):
        m = ''
        for i, q in zip(self.cart_item, self.cart_item_quantity):
            m += f'{i} x {q}kg = {i.price * q} ₴\n'
        return m


order = Order(customer3)
order.add_to_cart(apple, 2)
order.add_to_cart(banana, 1)

print(order)
