import random


class Product():
    """
    Class to maintain attributes of a product sold here at Acme Corporation
    """
    def __init__(self, input_name):
        """
        declares and initializes attributes for the class product.
        """
        self.name = input_name
        self.price = 10
        self.weight = 20
        self.flammability = 0.5
        self.identifier = random.randint(1000000, 9999999)

    def stealability(self):
        """
        Determines the ability for an Acme Corporation item to be stolen. This
        is based off the price divided by the weight.
        Returns:
        string
        """
        steal = float(self.price) / self.weight
        if(steal < 0.5):
            return "Not so stealable..."
        elif(steal >= 0.5 and steal < 1):
            return "Kinda stealable."
        else:
            return "Very stealable!"

    def explode(self):
        """
        Determines whether an Acme Corporation product will explode. This is
        based off of flammability times the weight.
        Returns:
        string
        """
        explodes = self.flammability * self.weight
        if(explodes < 10):
            return "...fizzle."
        elif(explodes >= 10 and explodes < 50):
            return "...boom!"
        else:
            return "...BABOOM!!"


class BoxingGlove(Product):
    def __init__(self, input_name):
        super().__init__(input_name)
        self.weight = 10

    def explode(self):
        """Boxing gloves don't explode"""
        return "...it's a glove."

    def punch(self):
        if(self.weight < 5):
            return "That tickles."
        elif(self.weight >= 5 and self.weight < 15):
            return "Hey that hurt!"
        else:
            return "OUCH!"
