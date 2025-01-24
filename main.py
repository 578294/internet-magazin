# Управление заказами в интернет-магазине

class Product:
    id_counter = 1

    def __init__(self, name, price, id):
        self.name = name
        self.price = price
        self.id = Product.id
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

    def add_orders(self, orders: Order):
        self.orders.append(orders)

    def remove_orders(self, order_id):
        self.orders = [i for i in self.orders if i.id != order_id]

    def change_status(self, new_status):
        self.status = new_status

    def calculate_total(self):
        return sum(product.price for order in self.orders)