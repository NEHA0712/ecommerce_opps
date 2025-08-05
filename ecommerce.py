from datetime import datetime

class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} (${self.price:.2f})"
-
class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.name} ({self.email})"

class Order:
    def __init__(self, order_id, customer):
        self.order_id = order_id
        self.customer = customer
        self.items = []
        self.created_at = datetime.now()

    def add_product(self, product, quantity=1):
        self.items.append({
            'product': product,
            'quantity': quantity
        })

    def total_price(self):
        return sum(item['product'].price * item['quantity'] for item in self.items)

    def __str__(self):
        summary = f"Order #{self.order_id}\nCustomer: {self.customer}\nDate: {self.created_at.strftime('%Y-%m-%d')}\n\nItems:\n"
        for item in self.items:
            product = item['product']
            quantity = item['quantity']
            total = product.price * quantity
            summary += f"- {product.name} x {quantity} = ${total:.2f}\n"
        summary += f"\nTotal: ${self.total_price():.2f}"
        return summary

def main():
    # Products
    p1 = Product(1, "Smartphone", 699.99)
    p2 = Product(2, "Headphones", 199.99)
    p3 = Product(3, "Charger", 29.99)

    # Customer
    customer = Customer(1, "John Doe", "john@example.com")

    # Order
    order = Order(101, customer)
    order.add_product(p1, 1)
    order.add_product(p2, 2)
    order.add_product(p3, 3)

    # Display Order
    print(order)

if __name__ == "__main__":
    main()
