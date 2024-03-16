from policyholder import Policyholder
from product import Product
from payment import Payment

# Create policyholders
policyholder1 = Policyholder("Alice", "POL001")
policyholder2 = Policyholder("Bob", "POL002")

# Create products
product1 = Product("Health Insurance", 100)
product2 = Product("Car Insurance", 150)

# Display policyholder and product details
policyholder1.display_details()
product1.display_details()

# Payment processing
payment_processor = Payment()
try:
    payment_processor.process_payment(product1.price)
except Exception as e:
    print("Payment processing failed:", str(e))
    # Here you can add further error handling or logging

# Display updated policyholder details
policyholder1.display_details()
