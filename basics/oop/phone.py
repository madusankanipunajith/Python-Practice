from item import Item


class Phone(Item):
    all = []

    def __init__(self, name: str, price: float, quantity: int = 0, broken_phone: int = 0):
        super().__init__(
            name, price, quantity
        )
        assert broken_phone >= 0, f'Broken Phones {broken_phone} is not gte to zero'

        self.broken_phone = broken_phone

        Phone.all.append(self)
