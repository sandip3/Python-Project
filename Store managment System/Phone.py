from Item import Item

class Phone(Item):

    def __init__(self, name: str, price: int, quntity=0, broken_phone=0):
        # call Super function to access all attribute / method of Item
        super().__init__(name, price, quntity)

        # run validatation to recived argument
        assert (
            broken_phone
        ), f"Given value of Broken Phone : {broken_phone} ,is not Greater then ot equal to Zero"

        # Assign to self Object
        self.broken_phone = broken_phone
        
