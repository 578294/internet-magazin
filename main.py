# Управление заказами в интернет-магазине
from itertools import product


class Product:
    id_counter = 1

    def __init__(self, name, price, id):
        self.name = name
        self.price = price
        self.id = id
        Product.id_counter += 1

    def __str__(self):
        return f"Product(Name: {self.name}, Price: {self.price}, ID: {self.id})"

class Order:
    def __init__(self):
        self.products = []
        self.status = "Новый"

    def add_product(self, product: Product):
        self.products.append(product)

    def remove_product(self, product_id):
        self.products = [i for i in self.products if i.id != product_id]

    def change_status(self, new_status):
        self.status = new_status

    def calculate_total(self):
        return sum(product.price for product in self.products)

    def __str__(self):
        products_list = ", ".join(self.products)
        return f"Order(Status: {self.status}, Total: {self.calculate_total()}, Products: {products_list}"

class Shop:
    def __init__(self):
        self.products = []
        self.orders = []
        self.status = "Новый"

    def add_product(self, product: Product):
        self.products.append(product)

    def remove_product(self, product_id):
        self.products = [i for i in self.products if i.id != product_id]

    def create_orders(self):
        new_order = Order()
        self.orders.append(new_order)
        return new_order

    def remove_orders(self, order_id):
        self.orders = [i for i in self.orders if i.id != order_id]

    def change_order_status(self, order_id, new_status):
        for order in self.orders:
            if order.id == order_id:
                order.change_status(new_status)
                break

    def calculate_total(self):
        return sum(order.calulate_total() for order in self.orders)

    def list_orders_by_status(self, status):
        return [order for order in self.orders if order.status == status]

    def __str__(self):
        products_list = "\n".join(str(product) for product in self.products)
        orders_list = "\n".join(str(order) for order in self.orders)
        return f"Shop: \nProducts:\n{products_list}\n{orders_list}"


product1 = Product("Попкорн", 570, 1)
product2 = Product("1 кг Говядины", 570, 2)
product3 = Product("Жареная кукуруза", 200, 3)

shop = Shop()

shop.add_product(product1)
shop.add_product(product2)
shop.add_product(product3)

order1 = shop.create_orders()
order1.add_product(product1)
order1.add_product(product2)

order2 = shop.create_orders()
order2.add_product(product3)

shop.change_order_status(order1, "В процессе")

print(shop)

print("\nЗаказы в процессе:")
for order in shop.list_orders_by_status("В процессе"):
    print(order)

print(f"\nОбщая выручка магазина: {shop.calculate_total()} руб.")
