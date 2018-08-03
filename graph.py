
# INSTRUCTIONS:
# How to run this file: In your terminal, do
# python graph.py < states.csv


from pprint import pprint
import fileinput
# TODO: What module needs to be imported here to work with files?
# TODO: Create an empty dictionary called hand_borders



# TODO: Now fill that dictionary in a way so if someone wants to know the
# states that border, say, "Georgia", they get back a list of the states
# ["Florida", "Alabama", "Tennessee", "North Carolina", "South Carolina"]

# TODO: Add in lists of states for each of the following states and the states:
Georgia = {"Alabama", "Florida", "South Carolina", "Tennessee", "North Carolina"}
Florida = {"Alabama", "Georgia"}
Alabama = {"Georgia", "Florida", "Mississippi", "Tennessee"}
Mississippi = {"Alabama", "Tennessee"}
SouthCarolina = {"North Carolina", "Georgia"}
NorthCarolina = {"Georgia", "South Carolina", "Tennessee"}
Tennessee = {"North Carolina", "Georgia", "Alabama", "Mississippi"}

hand_borders = {"Georgia" :	 Georgia, "Florida" : Florida, 
"Alabama" : Alabama, "Mississippi" : Mississippi, "South Carolina" : SouthCarolina, 
"Tennessee" : Tennessee, "North Carolina" : NorthCarolina }
# HINT: Use states.csv to help you remember which states share borders.


# TODO: Enumerate over the file input, print the line and the line number like
# in the example slides. Make sure you understand how this works.
borders = {}
for index, line in enumerate(fileinput.input()):
	print(str(index) + " ---- " + line)
	if(index == 0):
		print()
	else:
		line = line.strip()
		state = line.split(", ")
		if state[0] in borders:
			borders[state[0]].add(state[1])
		else:
			borders[state[0]] = {state[1]}
# With each line (except the first), use the string split function to split
# the line and extract the two states in each line
# Add each pair of states to a new dict called "borders"


	


# This is called "pretty print", see how it compares to just "print"
print("====================== MY MAP ======================")
pprint(hand_borders)

print()
print("====================== TRUE MAP ======================")
pprint(borders)

# TODO: If you did this correctly, both dicts should be the same
assert hand_borders == borders
