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

    def apply_increment(self, value):
        self.__price += self.__price * value

    def apply_discount(self):
        self.__price = self.__price * Item.pay_rate  # class level pay_rate but not instance level

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long")
        else:
            self.__name = value

    def calc_total_price(self):
        return self.__price * self.quantity

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.__price}, {self.quantity})"


class Phone(Item):
    all = []

    def __init__(self, name: str, price: float, quantity: int = 0, broken_phone: int = 0):
        super().__init__(
            name, price, quantity
        )
        assert broken_phone >= 0, f'Broken Phones {broken_phone} is not gte to zero'

        self.broken_phone = broken_phone

        Phone.all.append(self)


class Keyboard(Item):
    pay_rate = 0.8

    def __init__(self, name: str, price: float, quantity: int = 0):
        super().__init__(
            name, price, quantity
        )


phone01 = Phone('Etel', 2000, 20)
keyboard01 = Keyboard('Logitech', 2000, 6)
phone01.apply_discount()
print(phone01.price)
keyboard01.apply_discount()
# This is not change since we have used Item.pay_rate. but if we have used self.pay_rate
# this will be changed
print(keyboard01.price)
