'''
This program is used to demonstrate how loops in Python work.
'''

# This code prints out the numbers 0 through 5 in ascending order.
# The range() function returns a list of numbers that is the size of
# the number in parenthesis, counting upwards starting from zero.
# TODO: Change the code so that it prints out all numbers up to a value
#       that the user inputs.
max = int(input("Enter a max number"))
print()

for x in range(max):
    print (x)

mylist = [] #Creates an empty list called mylist

# A for loop iterates over a set number of items. A while loop continues looping
# until a certain condition is no longer met.
inputstring = input("Add a string to the list, or type Exit: ")

# This will continue looping as long as long as inputstring does not equal "Exit"
while inputstring != "Exit":
    #TODO: Add a statement that appends the new inputstring to mylist
    inputstring = input("Add a string to the list, or type Exit: ")
    mylist.append(inputstring)

# Prints out the size of the list. The format function replaces the brackets
# with the relavent variable
print("There are {} items is mylist".format(len(mylist)))

print() #This is just to create a new line

# TODO: A for loop can iterate over any list, not just lists created by the
#       range() function. Create a for loop to print out all of the strings
#       contained in mylist.

for x in mylist:
  print(x)

# A break statement can be used to terminate a loop.
counter = 0
while True:
      counter += 1 #Adds 1 to the variable counter
      print(counter, end=' ')
      if counter == 5:
          break
      
#TODO: Uncomment this while loop (remove the apostrophes) and then add a break so
#      it is no longer an infinite loop.

while True: #Creates an infinite loop
      print("You're stuck here forever!")
      break;


print() #This is just to create a new line

# A continue statement is used to run another pass thorugh the loop without
# Completeing the current pass.
for x in range(5):
      #TODO: Add a continue statement so that this loop prints nothing not "nothing"
      continue;
      print("nothing")




