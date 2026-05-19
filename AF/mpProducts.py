from products import FraudValidator, ReceiptGenerator, PaymentProcessor

class MpPaymentProcessor(PaymentProcessor):

    def pay(self, amount):
        print("Procesando el pago con MP: ${}".format(amount))
    
class MpFraudValidator(FraudValidator):

    def validate(self, amount):
        print("Procesando la validacion del pago con MP")
        return True
    
class MpReceiptGenerator(ReceiptGenerator):

    def generate(self, amount):
        print("Recibo de MP generado por ${}".format(amount))