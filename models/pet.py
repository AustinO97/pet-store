class Pet:
    def __init__(self, name, breed, price, pet_type_id, id = None):
        self.id = id
        self.name = name
        self.breed = breed
        self.price = price
        self.pet_type_id = pet_type_id

    def __repr__(self):
        return f'<Petid {self.id}: {self.name}, {self.breed}, {self.price}, pet_type_id={self.pet_type_id}>'
