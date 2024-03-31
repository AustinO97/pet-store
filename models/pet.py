class Pet:
    def __init__(self, name, breed, price):
        self.name = name
        self.breed = breed
        self.price = price

    def __repr__(self):
        return f"{self.name} ({self.breed}) - ${self.price}"