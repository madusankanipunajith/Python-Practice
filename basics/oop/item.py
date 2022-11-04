import csv


class Item:
    # class attribute
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received argument
        assert price > 0, f'price {price} is not greater than zero'
        assert quantity >= 0, f'quantity {quantity} is not greater than or equal to zero'

        # Assign to self object
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long")
        else:
            self.__name = value

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    def calc_total_price(self):
        return self.__price * self.quantity

    def apply_discount(self):
        self.__price = self.__price * Item.pay_rate  # class level pay_rate but not instance level

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.__price}, {self.quantity})"



