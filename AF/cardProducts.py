from products import FraudValidator, ReceiptGenerator, PaymentProcessor

class CardPaymentProcessor(PaymentProcessor):

    def pay(self, amount):
        print("Procesando el pago con tarjeta: ${}".format(amount))
    
class CardFraudValidator(FraudValidator):

    def validate(self, amount):
        print("Procesando la validacion del pago con la tarjeta")
        return True
    
class CardReceiptGenerator(ReceiptGenerator):

    def generate(self, amount):
        print("Recibo de la tarjeta generado por ${}".format(amount))