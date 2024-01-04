from datetime import date

class Product:
    def __init__(self, name: str, category: str, provider: 'Provider', price: float):
        self.name = name
        self.category = category
        self.provider = provider
        self.elements = []
        self.price = price

class Order:
    def __init__(self, number: int, timestamp: date, customer: 'Customer'):
        self.number = number
        self.timestamp = timestamp
        self.products = []
        self.customer = customer
        self.sum = 0

    def add_product(self, product: 'Product', quantity: int):
        self.products.append({
            "product": product,
            "quantity": quantity
        })
        self.sum += product.price * quantity

class Provider:
    def __init__(self, company: str, inn: str, email: str, phone: str, address: str):
        self.company = company
        self.inn = inn
        self.email = email
        self.phone = phone
        self.address = address

class Customer:
    def __init__(self, name: str, email: str, phone: str, address: str):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

# Приклад використання

# Створення постачальника
provider = Provider("ABC Company", "1234567890", "provider@example.com", "1234567890", "123 Main St")

# Створення товару
product1 = Product("Product 1", "Category 1", provider, 10.99)
product2 = Product("Product 2", "Category 2", provider, 20.99)

# Створення покупця
customer = Customer("John Doe", "customer@example.com", "9876543210", "456 Park Ave")

# Створення замовлення
order = Order(1, date.today(), customer)

# Додавання товарів до замовлення
order.add_product(product1, 2)
order.add_product(product2, 1)

# Виведення суми замовлення
print("Order total:", order.sum)