def factorial(n):
	if(n==1):
		return 1
	else:
		return factorial(n-1) * n
try:
	print("Enter a number: ");
	num = int(input())
	if(num != 0):
		print(factorial(num))
	else:
		print(1)
except ValueError:
	print(0)