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
        product_list = ", ".join(products)
        return f"Order(Status: {self.status}, Total: {self.calculate_total()}, Products: {products_list}"
