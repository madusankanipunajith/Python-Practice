from item import Item
from phone import Phone

item1 = Item("Phone", 110, 5)
item2 = Item("Calculator", 10, 5)
item3 = Item("Laptop", 400, 5)
item4 = Item("Watch", 20, 5)
item5 = Item("PC", 160, 5)
phone1 = Phone("Phone01", 290, 6, 3)

print(item1.name)
print(item1.price)
print(item1.calc_total_price())
print(item1.pay_rate)
print(Item.pay_rate)

print(Item.__dict__)  # all the attribute in class level
print(item1.__dict__)  # all the attribute in instance level

print(item1)  # using the magic method called __repr__
# print(Item.all)  # using the magic method called __repr__

Item.instantiate_from_csv()
print(Item.all)
print(Phone.all)

# Make attribute not accessible
print(phone1.name)



