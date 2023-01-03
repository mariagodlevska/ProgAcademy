# class that describes the shop items

import Exceptions


class ShopItems:
    def __init__(self, fruit: str, price: float, description: str):
        if price < 0:
            raise Exceptions.NegativePriceError(price, fruit)

        self.price = price
        self.description = description
        self.fruit = fruit

    def __str__(self):
        return f'{self.fruit}\nkind: {self.description}\nprice: {self.price}'
