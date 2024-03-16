class Product:
    def __init__(self, name, price, is_active=True):
        self.name = name
        self.price = price
        self.is_active = is_active

    def suspend(self):
        self.is_active = False

    def reactivate(self):
        self.is_active = True

    def display_details(self):
        print(f"Product Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Status: {'Active' if self.is_active else 'Suspended'}")
