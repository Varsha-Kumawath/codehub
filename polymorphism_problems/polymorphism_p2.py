class Payment:
    def process_payment(self):
        return f"Payment"

class CreditCardPayment(Payment):
    def process_payment(self):
        return f"Processing credit card payment "

class PayPalPayment(Payment):
    def process_payment(self):
          return f"Processing PayPalPayment"

class BitcoinPayment (Payment):
    def process_payment(self):
           return f"Processing BitcoinPayment"

# Function to process payment dynamically (Runtime Polymorphism)\
def display_payments(payment_method):
    return payment_method.process_payment()

CC=CreditCardPayment()
print(display_payments(CC))