# Рознесіть класи, які використовували під час вирішення завдання про замовлення та групу студентів по модулям.
# Переконайтеся у працездатності проєктів.

import ShopItems
import customer
import cart

# test shop items

apple = ShopItems.ShopItems('apple', 40, 'red')
orange = ShopItems.ShopItems('orange', 80, 'Brazil')
banana = ShopItems.ShopItems('banana', 60, 'Thailand')

# test customers

customer1 = customer.Customer('Petro', 'Poroshenko', 380501234567)
customer2 = customer.Customer('Volodymyr', 'Zelenskiy', 380675678912)
customer3 = customer.Customer('Victor', 'Yushchenko', 380985673456)

# possible carts

try:
    order = cart.Order(customer3)
    order.add_to_cart(apple, 2)
    order.add_to_cart(banana, 1)
    print(order)

except Exception as error:
    print(error)
