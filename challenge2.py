
"""
Challenge #2:

We're going to determine the distance between a pair of points by creating a
function called dist().

Recall the Euclidean distance between two points:
https://www.cut-the-knot.org/pythagoras/DistanceFormula.shtml

INPUT:
x1, x2, y1, y2 - the two pairs of coordinates

OUTPUT:
the float distance of between the two points

Examples:

dist(0, 0, 3, 4)  -- 5
dist(2, 2, 10, 17)  -- 17
dist(7, 0, 12, 12)  -- 13
"""
import math
def dist(x1, y1, x2, y2):
	return math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))


# These will test if your function works properly.
assert dist(0, 0, 3, 4) == 5
assert dist(2, 2, 10, 17) == 17
assert dist(7, 0, 12, 12) == 13


