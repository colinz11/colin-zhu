"""
Challenge #4:

We're going to investigate suspects in a crime and
determine which ones are guilty and which ones are free to go. Name the
function suspect()

INPUT:
initials  --  a string with initials of suspects, separated by spaces

familiar  -- a list of booleans inidicating whether the respective suspect
looks familiar to the victim


OUTPUT:
mistaken  -- a list of initials that were falsely accused,
meaning the index corresponding to their familiarity was
false

guilty  -- the list of indices indicating the indices of
guilty suspects


Examples:

suspect("OS JW ET", [True, True, False]) -- (["ET"], [0, 1])
suspect("AAA MJ BO", [False, False, False]) -- (["AAA", "MJ", "BO"], [])
suspect("MOS OS OSX", [False, False, True]) -- (["MOS", "OS"], [2])

HINT:
You will be returning multiple things, you can return them
as a tuple.
"""
def suspect(initals, familiar):
	sus = ([],[])
	for x in range(len(familiar)):
		if familiar[x]:
			sus[1].append(x)
		else:
			sus[0].append(initals.split(" ")[x])
	return sus

# These will test if your function works properly.
assert suspect("OS JW ET", [True, True, False]) == (["ET"], [0, 1])
assert suspect("AAA MJ BO", [False, False, False]) == (["AAA", "MJ", "BO"], [])
assert suspect("MOS OS OSX", [False, False, True]) == (["MOS", "OS"], [2])


