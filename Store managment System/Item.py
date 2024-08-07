import csv

class Item:

    pay_rate = 0.7  # pay_rate is price of product after applying 30% Off On sale and paying price is only 70%
    all = []

    def __init__(self, name: str, price: int, quntity=0):
        # run validatation to recived argument
        assert (
            price
        ), f"Given value of Price : {print} ,is not Greater then ot equal to Zero"
        assert (
            quntity
        ), f"Given value of Quntity : {quntity} ,is not Greater then ot equal to Zero"

        # Assign to self Object
        self.__name = name
        self.__price = price
        self.quntity = quntity

        # action to perform
        Item.all.append(self)

    @property
    # property decorator = Read only Attribute
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        self.__name = value

    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self,value):
        self.__price = self.__price + self.__price * value

    def totle_cost(self):
        print(f'\nTotal Cost of "{self.name}" : {self.__price * self.quntity}')

    @classmethod
    def instantiate_from_csv(cls):
        with open("./Items.csv") as File:
            data = csv.DictReader(File)
            items = list(data)

        for i in items:
            # print(i)
            Item(
                name=i.get("name"),
                price=float(i.get("price")),
                quntity=float(i.get("quntity")),
            )

    @staticmethod
    def is_numeric_integer(num):
        # we will count out all floats that are point zero
        # ex : 5.0 , 10.0

        if isinstance(num, float):
            # Count out float that are point zero
            return num.is_integer
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.name}", {self.__price}, {self.quntity})'
