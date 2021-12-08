class definitionModule:
    def init(self, name="", amount=0, price=0.00,calculatedPrice=0.00):
        self.name = name
        self.amount = amount
        self.price = self.price()
        self.calculatedPrice = self.totalPrice()

    def priceList(self):
     if self.name == "Dry Cured Iberian Ham":
         self.price = 177.80
     elif self.name =="Wagyu Steaks":
         self.price = 450.00
     elif self.name == "Matsutake Mushrooms":
         self.price = 272.00
     elif self.name == "Kopi Luwak Coffee":
         self.price = 306.50
     elif self.name == "Moose Cheese":
         self.price = 487.20
     elif self.name == "White Truffles":
         self.price = 3600.00
     elif self.name == "Blue Fin Tuna":
         self.price = 3603.00
     elif self.name == "Le Bonnotte Potatoes":
         self.price = 270.81
     else:
        self.price = 0.00

    def getName(self):
        return self.name
    def getAmount(self):
        return self.amount
    def getPrice(self):
        return self.price
    def getcalculatedPrice(self):
        return self.calculatedPrice

    def totalPrice(self):
        self.calculatedPrice = self.amount * self.price
        return self.calculatedPrice
