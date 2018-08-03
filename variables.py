# This is a comment, it's not intepreted by python
# it's here only for you to understand a piece of code.

# INSTRUCTIONS: Search for all the TODO lines and follow the directions
# provided.

print("This is a message that you will see in the terminal")
print("This message was not stored in a variable")

# Strings - sequences of characters
# Change the value below to your name.
print("================================")
name = "Ian"
print(name)

# TODO: Create a variable below called "message" with the message
# "This is from a variable called message" and print it
print("================================")


# Integers - numbers without any decimal points
# TODO: Write in your actual age here
print("================================")
age = 16
print("My age is: ")
# TODO: Make the line below print your actual age using the age variable
print(age)

# Floats -- numbers with decimal points in them
print("================================")
pi = 3.14159
print("The value of pi is: ", pi)

# TODO: Print out the value of pi


# We can make comparisons with numeric types too
print("================================")
print("Are you old enough to vote?")
print(age > 17)


print("Are you old enough for a driver's permit?")
print(age >= 15)


# TODO: Fix this line so it prints out the value of pi.
# Can you think of why it might be crashing?
print("================================")
print(pi)


# We can use the "assignment operator" to change the value of any variable:
print("================================")
age += 2
print(age)

# Here's another notation we can use, it does the same thing
print("================================")
age += 3
print(age)

# TODO: Reset age to its original value using subtraction
print("================================")
age -= 5
print(age)


# Assignment and checking for equality are two totally different
# things. Here we use two equal signs, which checks for equality
print("================================")
print(pi == 3.14159)


# The keyword "is" can be a bit tricky because it's checking if two
# things are stored in the same place, not necessarily if they are
# equal in value
print("================================")
anotha_pi = pi + 1
anotha_pi -= 1
print("'pi is anotha_pi' will evaluate to False:")
print(pi is anotha_pi)

print("================================")
# Sometimes it acts funny. As shown below.
# TAKEAWAY: Generally avoid "is", use == whenever possible to check values
three  = 3
more_three  = three + 1
more_three -= 1

print("'three == more_three' will evaluate to True:")
print(three == more_three)

print("'three is more_three' will evaluate to True:")
print(three is more_three)


# Booleans -- True or False
# We can also store True or False in a variable, these types are
# called boolean
eligible_voter = age >= 18
print("================================")
print("Are you of voting age?")
print(eligible_voter)

# Set the variable below to True using assignment operator
print("================================")
print("Booleans")
assignment_completed = False
print(assignment_completed)

# We can also flip the value of the value of assignment_completed another way
print("================================")
print("Before the flip:")
print(assignment_completed)

assignment_completed = not assignment_completed
print("Boolean value is now flipped from above:")
print(assignment_completed)


# Functions -- these can be executed directly
print("================================")
def gimme_zero():
    return 0

zero = gimme_zero()
print("Will give you zero:")
print(zero)


print("================================")
def gimme_two_numbers():
    return 0, 1

two_numbers = gimme_two_numbers()
print("Will give you (0, 1) -- this is called a tuple")
print(two_numbers)
