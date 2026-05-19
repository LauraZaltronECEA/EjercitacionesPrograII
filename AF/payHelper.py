def checkout(factory, amount):
    validator = factory.create_fraud_validator()

    if not validator.validate(amount):
        raise Exception("Pago rechazado")
    
    processor = factory.create_payment_processor()
    processor.pay(amount)

    receipt = factory.create_receipt_generator()
    receipt.generate(amount)