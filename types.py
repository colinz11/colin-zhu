# TODO: Replace below with your team name
team_name = "Go England!"
print("Team name: ")
print(team_name)

# The lines above define a variable called "team_name".
# Letter case and spacing all matter, so make sure you type
# the variable names correctly.

# TODO: Correct the print statement below so the code runs
# without crashing.
print("================================")
course_name = "Artificial Intelligence"
print(course_name)

# TODO: Which data type should this be to make the statement print True?
# Uncomment the line below and replace "bool" with the true data type
print("================================")
print("Next line should print True")
print(isinstance(team_name, str))



# TODO: Change the data type below so the statement prints True
print("================================")
print("Next line should print True")
print(isinstance(7, int))

# TODO: Change the data type below so the statement prints True
print("================================")
print("Next line should print True")
print(isinstance(7.33333, float))


def add(a, b):
    # TODO: Make this function return the sum of aand b
    
    return a+b

# We'll use this to verify that you implemented add() properly.
print("================================")
print("This should be 7:")
print(add(3, 4))

def divide(a, b):
    # TODO: Make this function return a divided by b
	if b == 0:
		return "Cannot divide by 0"
	elif a % b == 0:
		return int(a/b)
	else:
		return a/b
# Division example 1
print("================================")
print("This should be 5")
print((divide(25, 5)))

# Division example 2
print("This should be 2.5")
print(divide(5, 2))

# TODO: Why is this crashing? Be prepared to explain in class.
print("================================")
print("This next line will crash")
print(divide(5, 0))



age = input()