class Coffee:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) < 3:
            raise ValueError("Coffee name must be a string with length at least 3 characters")
        self._name = name
        self.orders = []
        self.customers = []

    @property
    def name(self):
        return self._name

    def num_orders(self):
        return len(self.orders)

    def average_price(self):
        if not self.orders:
            return 0.0
        total_price = sum(order.price for order in self.orders)
        return total_price / len(self.orders)

    def customers(self):
        return list(set(order.customer for order in self.orders))


class Customer:
    def __init__(self, name):
        if not isinstance(name, str) or not (1 <= len(name) <= 15):
            raise ValueError("Customer name must be a string with length between 1 and 15 characters")
        self.name = name
        self.orders = []

    def num_orders(self):
        return len(self.orders)

    def average_price(self):
        if not self.orders:
            return 0.0
        total_price = sum(order.price for order in self.orders)
        return total_price / len(self.orders)

    def coffees(self):
        return list(set(order.coffee for order in self.orders))

    def create_order(self, coffee, price):
        if not isinstance(price, (int, float)) or not (1.0 <= price <= 10.0):
            raise ValueError("Price must be a number between 1.0 and 10.0")
        order = Order(self, coffee, price)
        return order


class Order:
    all_orders = []

    def __init__(self, customer, coffee, price):
        if not isinstance(price, (int, float)) or not (1.0 <= price <= 10.0):
            raise ValueError("Price must be a number between 1.0 and 10.0")
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all_orders.append(self)
        coffee.orders.append(self)
        customer.orders.append(self)
