from shoppingListRA import definitionModule #importing the class module to this file

def listofObject(): #function to create new list
    li = [] #empty list
    numberItems = 0 #used as variable in looping
    while numberItems < 1: #input the rule that number must be greater than 1
        numberItems = int(input("How many items will you order today?")) 
        print("The number of items purchases is at least 1") #print this if less than 1
    for i in range(numberItems):
        print(f"Item #{i+1}")
        name= input("Enter food name:")
        amount= input("Enter amount of pounds:")
        while amount <= 0: #amount must be greater than 0
            print("Amounts of pounds must be greater than 0.")
            amount = ("Enter amounts of pounds:") #re write available number
        li.append(definitionModule(name,amount,price,calculatedPrice))
    return li

def displayContent(list): #print every information that has been updated
         print("Here's a summary of the items purchased:")
         for displayContent in list:
             print(f"Items:{displayContent.getName()}")
             print(f"Amount ordered:{displayContent.getAmount()}pounds")
             print(f"Price per pound: ${displayContent.getPrice():.2f}")
             print(f"price of order: ${displayContent.getcalculatedPrice():.2f}")

def total(list): #count the total using formula
    total = 0
    for i in list:
        total = i.getcalculatedPrice + total
        print("Your total payment are: ${:.2f}".format(total))

def main():# print
    list = listofObject()
    displayContent(list)
    total(list)

main()


