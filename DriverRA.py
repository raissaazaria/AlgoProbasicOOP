from shoppingListRA import definitionModule

def listofObject():
    li = []
    numberItems = 0
    while numberItems < 1:
        numberItems = int(input("How many items will you order today?"))
        print("The number of items purchases is at least 1")
    for i in range(numberItems):
        print(f"Item #{i+1}")
        food= input("Enter food name:")
        amount= input("Enter amount of pounds:")
        while amount <= 0:
            print("Amounts of pounds must be greater than 0.")
            amount = ("Enter amounts of pounds:")
        li.append(definitionModule(food,amount))
    return li

def displayContent(list):
         print("Here's a summary of the items purchased:")
         for displayContent in list:
             print(f"Items:{displayContent.getName()}")
             print(f"Amount ordered:{displayContent.getAmount()}pounds")
             print(f"Price per pound: ${displayContent.getPrice():.2f}")
             print(f"price of order: ${displayContent.getcalculatedPrice():.2f}")

def total(list):
    total = 0
    for i in list:
        total = i.getcalculatedPrice + total
        print("Your total payment are: ${:.2f}".format(total))

def main():
    list = listofObject()
    displayContent(list)
    total(list)

main()


