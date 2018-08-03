def rev(string):
	newstring = ""
	for x in string:
		newstring = x + newstring
	return newstring

def revRec(string, newString):
	if (len(string) < 1):
		return newString
	else:
		return revRec(string[:-1], newString + string[len(string) - 1])

string = input("Enter a String: ")

print(str(rev(string)))
