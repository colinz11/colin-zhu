'''
Lists Problem: 
 Make a list of at least three types of pizza you enjoy.
   Store these in a list.
   In a for loop, print the name of each pizza.
   Modify the for loop so that you print a sentence along with the pizza type.
   e.g. "I like pepperoni pizza." or "Hawaiian is the devil."
   Make a copy of the list pizza, calling it friend_pizzas.
   Then add a new pizza to the original list, and add a different pizza to friend_pizzas.
   Make a new for loop for friend_pizzas, printing its contents.

Conditionals: 
Write an if-elif-else chain that determines a person’s 
stage of life. Set a value for the variable age, and then:
•	 If the person is less than 2 years old, print a message that the person is 
a baby.
•	 If the person is at least 2 years old but less than 4, print a message that 
the person is a toddler.
•	 If the person is at least 4 years old but less than 13, print a message that 
the person is a kid.
•	 If the person is at least 13 years old but less than 20, print a message that 
the person is a teenager.
•	 If the person is at least 20 years old but less than 65, print a message that 
the person is an adult.
•	 If the person is age 65 or older, print a message that the person is an 
elder.

For loops:
   Make a loop that iterates through the numbers one to one thousand.
   Edit your program so that at the end it prints the sum of all numbers one to one thousand.
   Expand the numbers from one to one thousand to one to one million.
'''
'''
pizza = ["Cheese", "Pineapple", "Mushroom"]
friend_pizzas = pizza.copy()
pizza.append("Pepperoni")
for type in pizza:
   print("I like {0} pizza".format(type))

friend_pizzas.append("Vegetarian")
for type in friend_pizzas:
   print("You like {0} pizza".format(type))
'''

'''
age = 64
if age < 2:
   print("baby")
elif age < 4:
   print("toddler")
elif age < 13:
   print('kid')
elif age < 20:
   print("teenager")
elif age < 65:
   print("adult")
else:
   print("elder")
'''
sum = 0
for x in range(1, 1000001):
   sum += x
print(sum)





   