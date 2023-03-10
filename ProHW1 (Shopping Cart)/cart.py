# class that describes the orders in cart (with a number of products and a customer)

import ShopItems
import customer


class Order:
    def __init__(self, customer: customer):
        self.customer = customer
        self.cart_item = []
        self.cart_item_quantity = []
        self.iter = 0

    def __next__(self):
        if self.iter >= len(self.cart_item):
            raise StopIteration
        else:
            self.iter += 1
            return self.cart_item[self.iter - 1]

    def __iter__(self):
        return self

    def __getitem__(self, item):
        if item is int:
            return self.cart_item[item]
        else:
            raise TypeError

    def add_to_cart(self, product: ShopItems, quantity=1):
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
        m = []
        for i, q in zip(self.cart_item, self.cart_item_quantity):
            m.append(f'{i} x {q}kg = {i.price * q} ₴')
        return '\n'.join(m)
