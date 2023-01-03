class NegativePriceError(Exception):
    def __init__(self, price, fruit):
        self.price = price
        self.fruit = fruit

    def __str__(self):
        return f'Price ({self.price}) of {self.fruit} is negative. Please check the price.'
