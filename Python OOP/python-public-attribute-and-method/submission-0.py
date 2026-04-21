class StoreItem:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price
        
chips = StoreItem("Chips", 1.99) # Don't modify this line

print(chips.name)
print(chips.price)

