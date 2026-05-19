from products import FraudValidator, ReceiptGenerator, PaymentProcessor

class PaypalPaymentProcessor(PaymentProcessor):

    def pay(self, amount):
        print("Procesando el pago con paypal: ${}".format(amount))
    
class PaypalFraudValidator(FraudValidator):

    def validate(self, amount):
        print("Procesando la validacion del pago con paypal")
        return True
    
class PaypalReceiptGenerator(ReceiptGenerator):

    def generate(self, amount):
        print("Recibo de paypal generado por ${}".format(amount))