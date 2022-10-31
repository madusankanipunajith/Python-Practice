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

    # hiding methods from user
    def __send(self):
        pass

    def __prepare_body(self):
        return f'Hello madusanka. We have {self.__name} {self.quantity} times' \
               f'Regards, peter'

    def __connect(self):
        pass

    def send_email(self):
        self.__connect()
        self.__prepare_body()
        self.__send()

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.__price}, {self.quantity})"


item1 = Item("myItem", 200, 6)
print(item1.price)
item1.apply_discount()
print(item1.price)
item1.apply_increment(0.2)
print(item1.price)
