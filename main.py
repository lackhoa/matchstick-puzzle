from itertools import combinations

# Input: Each shape is identified by a set matchsticks. Each matchstick is in turn indicated by two points. Each point is then indicated by its coordinates. Note: The first point must be to the left and/or on top of the second point
# This program can solve problems with non-directional units like coins (like in the third puzzle). It's just that the points of each "matchstick" have the same coordinates

# The fish puzzle
# Shape number one:
# first_shape = {((0,0),(1,0)), ((0,1),(1,1)), ((1,0),(1,1)), ((1,0),(2,0)), ((1,1),(1,2)), ((1,1),(2,1)), ((2,0),(2,1)), ((2,1),(2,2))}
# Shape number two:
# second_shape = {((0,0),(0,1)), ((0,1),(0,2)), ((0,1),(1,1)), ((0,2),(1,2)), ((1,0),(1,1)), ((1,1),(1,2)), ((1,1),(2,1)), ((1,2),(2,2))}
#------------------------------------------------------------
# The triangle puzzle
# Shape number one:
# first_shape = {((0,3),(1,2)), ((0,3),(1,4)), ((1,2),(2,1)), ((1,2),(2,3)), ((1,4),(2,3)), ((1,4),(2,5)), ((2,1),(3,0)), ((2,1),(3,2)), ((2,3),(3,2)), ((2,3),(3,4)), ((2,5),(3,4)), ((2,5),(3,6))}
# second_shape = {((0,0),(1,1)), ((0,2),(1,1)), ((0,2),(1,3)), ((0,4),(1,3)), ((0,4),(1,5)), ((1,1),(2,2)), ((1,3),(2,2)), ((1,3),(2,4)), ((2,2),(3,3)), ((2,4),(3,3))}
#------------------------------------------------------------
# The triangle puzzle (with coins)
# Shape number one:
first_shape = {((0,3),(0,3)), ((1,2),(1,2)), ((1,4),(1,4)), ((2,1),(2,1)), ((2,3),(2,3)), ((2,5),(2,5)), ((3,0),(3,0)), ((3,2),(3,2)), ((3,4),(3,4)), ((3,6),(3,6))}
second_shape = {((0,0),(0,0)), ((0,2),(0,2)), ((0,4),(0,4)), ((0,6),(0,6)), ((1,1),(1,1)), ((1,3),(1,3)), ((1,5),(1,5)), ((2,2),(2,2)), ((2,4),(2,4)), ((3,3),(3,3))}


# Compression algorithm: drag the shape to the left-most and top-most position for ease of comparison
def compress(set_in):
	# find the minimum x-coordinate and y-coordinate:
	min_x = 1000
	min_y = 1000
	for s in set_in:
		min_x_local = min(s[0][0], s[1][0])
		if min_x_local < min_x:
			min_x = min_x_local
		min_y_local = min(s[0][1], s[1][1])
		if min_y_local < min_y:
			min_y = min_y_local

	# Return a new result:
	# Nothing changes if the input is in the correct format
	result = set()

	if (min_x_local == 0) and (min_y_local == 0):
		result = set_in
	# Else
	else:
		result = set()
		for s in set_in:
			result.add(((s[0][0] - min_x, s[0][1] - min_y), (s[1][0] - min_x, s[1][1] - min_y)))

	return result

# The main algorithm:
counter = 0
n = len(first_shape)
for i in range(1, n - 1):
	for s1 in combinations(first_shape, n - i):
		for s2 in combinations(second_shape, n - i):
			s1 = set(compress(s1))
			s2 = set(compress(s2))

			if s1.difference(s2) == set(): # If those are identical
				print("#"+str(counter)+" " + str(s1)) # print the result
				counter += 1

print("Total results count: " + str(counter))