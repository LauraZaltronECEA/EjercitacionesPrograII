from Factories import MPFactory, CardFactory, PayPalFactory
from payHelper import checkout

factory = PayPalFactory()
checkout(factory, 500000)
