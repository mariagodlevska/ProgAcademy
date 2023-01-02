# 1. Модифікуйте Перше домашнє завдання так, щоб при спробі встановити від'ємну або нульову
# вартість товару викликалася виняткова ситуація (тип виняткової ситуації треба самостійно реалізувати).

# class that describes the shop items

class NegativePriceError(Exception):
    def __init__(self, price, fruit):
        self.price = price
        self.fruit = fruit

    def __str__(self):
        return f'Price ({self.price}) of {self.fruit} is negative. Please check the price.'


class ShopItems:
    def __init__(self, fruit: str, price: float, description: str):
        if price < 0:
            raise NegativePriceError(price, fruit)

        self.price = price
        self.description = description
        self.fruit = fruit



    def __str__(self):
        return f'{self.fruit}\nkind: {self.description}\nprice: {self.price}'


apple = ShopItems('apple', 40, 'red')
orange = ShopItems('orange', 80, 'Brazil')
banana = ShopItems('banana', -60, 'Thailand')

# class that describes the customers


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

# class that describes the orders in cart (with a number of products and a customer)


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

# possible carts

try:
    order = Order(customer3)
    order.add_to_cart(apple, 2)
    order.add_to_cart(banana, 1)
    print(order)

except Exception as error:
    print(error)



