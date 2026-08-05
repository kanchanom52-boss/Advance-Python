from abc import ABC, abstractmethod
from datetime import datetime
import uuid
from functools import wraps


# ---------------- Receipt ----------------

class Receipt:

    def __init__(self, amount, method, status):
        self.txn_id = str(uuid.uuid4())[:8]
        self.amount = amount
        self.method = method
        self.status = status
        self.time = datetime.now()

    def __str__(self):
        return (
            "\n========== RECEIPT ==========\n"
            f"Transaction ID : {self.txn_id}\n"
            f"Amount         : ₹{self.amount}\n"
            f"Method         : {self.method}\n"
            f"Status         : {self.status}\n"
            f"Time           : {self.time}\n"
            "=============================\n"
        )


# ---------------- Decorator ----------------

def log_transaction(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("\n[LOG] Payment Started...")
        result = func(*args, **kwargs)
        print("[LOG] Payment Completed.\n")
        return result

    return wrapper


# ---------------- Strategy ----------------

class PaymentStrategy(ABC):

    @abstractmethod
    def validate(self):
        pass

    @abstractmethod
    def pay(self, amount):
        pass


# ---------------- Credit Card ----------------

class CreditCardPayment(PaymentStrategy):

    def __init__(self, card, cvv, expiry):
        self.card = card
        self.cvv = cvv
        self.expiry = expiry

    def validate(self):
        return len(self.card) == 16 and len(self.cvv) == 3

    def pay(self, amount):

        if self.validate():
            return Receipt(amount, "Credit Card", "SUCCESS")

        return Receipt(amount, "Credit Card", "FAILED")


# ---------------- PayPal ----------------

class PayPalPayment(PaymentStrategy):

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def validate(self):
        return "@" in self.email

    def pay(self, amount):

        if self.validate():
            return Receipt(amount, "PayPal", "SUCCESS")

        return Receipt(amount, "PayPal", "FAILED")


# ---------------- UPI ----------------

class UPIPayment(PaymentStrategy):

    def __init__(self, upi):
        self.upi = upi

    def validate(self):
        return "@" in self.upi

    def pay(self, amount):

        if self.validate():
            return Receipt(amount, "UPI", "SUCCESS")

        return Receipt(amount, "UPI", "FAILED")


# ---------------- Net Banking ----------------

class NetBankingPayment(PaymentStrategy):

    def __init__(self, bank, account):
        self.bank = bank
        self.account = account

    def validate(self):
        return len(self.account) >= 8

    def pay(self, amount):

        if self.validate():
            return Receipt(amount, "Net Banking", "SUCCESS")

        return Receipt(amount, "Net Banking", "FAILED")




class PaymentProcessor:

    registry = {}

    def __init__(self, strategy=None):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    @log_transaction
    def process_payment(self, amount):

        if self.strategy is None:
            print("No Payment Method Selected")
            return

        return self.strategy.pay(amount)

    @classmethod
    def register_strategy(cls, key, strategy_class):
        cls.registry[key] = strategy_class

    @classmethod
    def create(cls, key, **kwargs):

        strategy = cls.registry[key](**kwargs)
        return cls(strategy)

    @classmethod
    def available_methods(cls):
        return cls.registry.keys()


# ---------------- Register ----------------

PaymentProcessor.register_strategy("credit", CreditCardPayment)
PaymentProcessor.register_strategy("paypal", PayPalPayment)
PaymentProcessor.register_strategy("upi", UPIPayment)
PaymentProcessor.register_strategy("netbank", NetBankingPayment)


# ---------------- Driver ----------------

while True:

    print("\n========= PAYMENT SYSTEM =========")
    print("1. UPI")
    print("2. Credit Card")
    print("3. PayPal")
    print("4. Net Banking")
    print("5. Exit")

    choice = input("Enter Choice : ")

    if choice == "5":
        print("Thank You")
        break

    amount = float(input("Enter Amount : "))

    if choice == "1":

        upi = input("Enter UPI ID : ")

        processor = PaymentProcessor.create(
            "upi",
            upi=upi
        )

    elif choice == "2":

        card = input("Enter Card Number : ")
        cvv = input("Enter CVV : ")
        expiry = input("Enter Expiry : ")

        processor = PaymentProcessor.create(
            "credit",
            card=card,
            cvv=cvv,
            expiry=expiry
        )

    elif choice == "3":

        email = input("Enter Email : ")
        password = input("Enter Password : ")

        processor = PaymentProcessor.create(
            "paypal",
            email=email,
            password=password
        )

    elif choice == "4":

        bank = input("Enter Bank Name : ")
        account = input("Enter Account Number : ")

        processor = PaymentProcessor.create(
            "netbank",
            bank=bank,
            account=account
        )

    else:
        print("Invalid Choice")
        continue

    receipt = processor.process_payment(amount)

    if receipt:
        print(receipt)

    ans = input("Do you want another payment? (y/n): ")

    if ans.lower() != "y":
        break