class definitionModule: #Class definition
    def init(self, name="", amount=0, price=0.00,calculatedPrice=0.00): #Initializer methods 
        self.__name = name #set hidden attributes
        self.__amount = amount
        self.__price = self.price()
        self.calculatedPrice = self.totalPrice() #set public attributes

    def priceList(self): #private list storing the list of menu
     if self.__name == "Dry Cured Iberian Ham":
         self.__price = 177.80
     elif self.__name =="Wagyu Steaks":
         self.__price = 450.00
     elif self.__name == "Matsutake Mushrooms":
         self.__price = 272.00
     elif self.__name == "Kopi Luwak Coffee":
         self.__price = 306.50
     elif self.__name == "Moose Cheese":
         self.__price = 487.20
     elif self.__name == "White Truffles":
         self.__price = 3600.00
     elif self.__name == "Blue Fin Tuna":
         self.__price = 3603.00
     elif self.__name == "Le Bonnotte Potatoes":
         self.__price = 270.81
     else: #other then the menu above, will count as 0
        self.__price = 0.00

    def getName(self): #accessor methods 
        return self.__name
    def getAmount(self):
        return self.__amount
    def getPrice(self):
        return self.__price
    def getcalculatedPrice(self):
        return self.calculatedPrice

    def totalPrice(self): #function to calculate the total
        self.calculatedPrice = self.__amount * self.__price
        return self.calculatedPrice
