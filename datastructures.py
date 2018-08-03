
# ===========================
#           SETS
# ===========================


# TODO: Create a list of 5 different fruits, call it basket.
basket = ["Apple", "Orange", "Kiwi", "Lemon", "Lime"]
print(basket)


# TODO: Create a new list of fruits called cart that has everything basket
# has, but even more, and some duplicates.
cart = ["Apple", "Apple", "Melen", "Cherry"] + basket
print(cart)


# TODO: Now, lets convert both cart and basket to sets
cart_set = set(cart)
basket_set = set(basket)

# TODO: Create a new variable called "both_set" that is the intersection
# of both sets.
both_set = cart_set.union(basket_set)
print(both_set)

# This will not crash when you've got everything above working.
assert both_set == cart_set

# Now create a set called outside_basket that includes only things in cart_set
# but not in basket_set
outside_basket = []
for fruit in cart:
	if(fruit not in basket_set):
		outside_basket.append(fruit)
print(outside_basket)


# TODO: Uncomment this when done with the above.
assert len(outside_basket) > 0


# ===========================
#           DICTIONARIES
# ===========================


# TODO: Create a dictionary called "prices" with a price assigned
# for each of the fruits in basket above.
prices = {"Apple" : 1, "Melen" : 2, "Cherry" : 3, "Orange" : 10, "Kiwi" : 12, "Lemon" : 15, "Lime" : 20}

print(prices)


# TODO: Complete the function. Make it iterate over the
# key and value of prices and print a line like "X cost $Y today, this is a great deal."
def price_check(prices):
    for fruit, price in prices.items():
    	print("{0} costs ${1} today, this is a great deal".format(fruit, price))


price_check(prices)


# TODO: Complete the function below called checkout, which takes a
# list called cart full of fruits and a dictionary and adds up the
# price of each item in the cart.
def checkout(cart, prices):
	price = 0
	for fruit in cart:
		price += prices[fruit]
	return price


# TODO: Sanity check the output below, it should make sense given
# your choice of numbers above.
print(checkout(cart, prices))
