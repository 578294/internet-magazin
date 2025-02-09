# Управление заказами в интернет-магазине

class Product:
    id_counter = 1

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.id = Product.id_counter
        Product.id_counter += 1

    def __str__(self):
        return f"Product(Name: {self.name}, Price: {self.price}, ID: {self.id})"


class Order:
    id_counter = 1

    def __init__(self):
        self.products = []
        self.status = "Новый"
        self.id = Order.id_counter
        Order.id_counter += 1

    def add_product(self, product: Product):
        self.products.append(product)

    def remove_product(self, product_id):
        self.products = [i for i in self.products if i.id != product_id]

    def change_status(self, new_status):
        self.status = new_status

    def calculate_total(self):
        return sum(product.price for product in self.products)

    def __str__(self):
        products_list = ", ".join(str(product) for product in self.products)
        return f"Order(ID: {self.id}, Status: {self.status}, Total: {self.calculate_total()}, Products: {products_list})"


class Shop:
    def __init__(self):
        self.products = []
        self.orders = []

    def add_product(self, product: Product):
        self.products.append(product)

    def remove_product(self, product_id):
        self.products = [i for i in self.products if i.id != product_id]

    def create_order(self):
        new_order = Order()
        self.orders.append(new_order)
        return new_order

    def remove_order(self, order_id):
        self.orders = [i for i in self.orders if i.id != order_id]

    def change_order_status(self, order_id, new_status):
        for order in self.orders:
            if order.id == order_id:
                order.change_status(new_status)
                break

    def calculate_total(self):
        return sum(order.calculate_total() for order in self.orders)

    def list_orders_by_status(self, status):
        return [order for order in self.orders if order.status == status]

    def __str__(self):
        products_list = "\n".join(str(product) for product in self.products)
        orders_list = "\n".join(str(order) for order in self.orders)
        return f"Shop:\nProducts:\n{products_list}\n\nOrders:\n{orders_list}"


# Создание товаров
product1 = Product("Попкорн", 570)
product2 = Product("1 кг Говядины", 570)
product3 = Product("Жареная кукуруза", 200)

shop = Shop()

# Добавление товаров в магазин
shop.add_product(product1)
shop.add_product(product2)
shop.add_product(product3)

# Создание заказов
order1 = shop.create_order()
order1.add_product(product1)
order1.add_product(product2)

order2 = shop.create_order()
order2.add_product(product3)

# Изменение статуса заказа
shop.change_order_status(order1.id, "В процессе")

print(shop)

print("\nЗаказы в процессе:")
for order in shop.list_orders_by_status("В процессе"):
    print(order)

print(f"\nОбщая выручка магазина: {shop.calculate_total()} руб.")
