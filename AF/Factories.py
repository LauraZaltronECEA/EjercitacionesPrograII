from AbstractFactories import PaymentFactory
from cardProducts import CardFraudValidator, CardPaymentProcessor, CardReceiptGenerator
from mpProducts import MpFraudValidator, MpPaymentProcessor, MpReceiptGenerator
from PaypalProducts import PaypalFraudValidator, PaypalPaymentProcessor, PaypalReceiptGenerator

class CardFactory(PaymentFactory):

    def create_fraud_validator(self):
        return CardFraudValidator()
    
    def create_payment_processor(self):
        return CardPaymentProcessor()
    
    def create_receipt_generator(self):
        return CardReceiptGenerator()

class MPFactory(PaymentFactory):

    def create_fraud_validator(self):
        return MpFraudValidator()
    
    def create_payment_processor(self):
        return MpPaymentProcessor()
    
    def create_receipt_generator(self):
        return MpReceiptGenerator() 
    
class PayPalFactory(PaymentFactory):

    def create_fraud_validator(self):
        return PaypalFraudValidator()
    
    def create_payment_processor(self):
        return PaypalPaymentProcessor()
    
    def create_receipt_generator(self):
        return PaypalReceiptGenerator() 