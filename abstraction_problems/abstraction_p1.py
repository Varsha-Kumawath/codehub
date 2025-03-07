from abc import ABC,abstractmethod

class PaymentGateway(ABC):
    # process_payment(amount) as an abstract method (must be implemented by subclasses).
    @abstractmethod
    def process_payment(self,amount):
       pass
    # validate_payment() as a concrete method (shared across all subclasses).
    def  validate_payment(self):
        print("validating Payment")


class CreditCardPayment(PaymentGateway):
    def process_payment(self, amount):
        return f"Processing credit card payment of ${amount}"

class UPIPayment(PaymentGateway):
    def process_payment(self, amount):
        return f"Processing UPI payment of ${amount}"

Cred=CreditCardPayment()
Cred.validate_payment()
print(Cred.process_payment(500))