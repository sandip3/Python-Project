from Item import Item
from Phone import Phone


# -------------------------------------------------------------

item1 = Item("Samsung", 50000, 7)


# print(item1.name)
# print(item1.price)

# item1.name = "Black Berry"
# item1.apply_increment(0.5)

# print(item1.name)
# print(item1.price)


# item1.read_only_name = "Pradip"
# print(item1.read_only_name)


# print(Item.all)
# print(Phone.all)

# -------------------------------------------------------------

# Item.instantiate_from_csv()
# print(Item.all)

# -------------------------------------------------------------

# item_1 = Item("Leptop", 50000, 7)
# item_2 = Item("Smart-phone", 30000, 10)
# item_3 = Item("Cable", 100, 4)
# item_4 = Item("Mouse", 500, 7)
# item_5 = Item("Keyborad", 600, 7)


# for instance in Item.all:
#     print(instance.name)


# -------------------------------------------------------------

# print(Item.__dict__) # Get all attribute From Class Lavel
# print(item_1.__dict__)  # Get all attribute From Instants Lavel
# print(item_2.__dict__)  # Get all attribute From Instants Lavel

# -------------------------------------------------------------

# item_1.totle_cost()
# item_2.totle_cost()

# -------------------------------------------------------------

# in this it's Instant Offer of 20% off sale it find Pay rate from instant
# item_1.pay_rate = 0.8 # Offer for Item is 20% off
# item_1.apply_discount()
# print(item_1.price)


# in this it's dynamic Offer of 30% off sale it find Pay rate from class
# print(f"\nBefore Sale Price : {item_2.price}")
# item_2.apply_discount()
# print(f"After Sale Price : {item_2.price}")

# -------------------------------------------------------------
