'''
This is a simple program to emulate a vending machine.
'''

# TODO: Create your own input message.
item = (input("What would you like to buy? "))



# TODO: Expand the number of recognized inputs to at least six, with at least four
#       different prices. Then add a print statement above that lists the recognized
#       items with their prices
if item == "coke" or item == "fanta":
    price = 1.5
elif item == "water":
    price = 1.0
elif item == "sprite":
    price = 2.0
elif item == "pepsi":
    price = 2.0
elif item == "coke zero":
    price = 2.5
elif item == "pepsi max":
    price = 2.7
else:
    print("Error: Unrecognized Input")
    exit(1)
print(item, ": $", price)
# The input() function returns the input as a string, the float() function
# then converts that string into a float.
payment = float(input("How much money do you enter into the machine? "))

# TODO: Find and repair the error in the following if-else statements.
#       Assume that payment is a number.
if payment < price:
    print ("Insufficient Funds")
elif payment == price:
    print ("You recieve a " + item + " and no change.")
else:
    #The str() function converts the float into a string
    print ("You recieve a " + item + " and $" + str(payment - price) + " in change.")
    







    
