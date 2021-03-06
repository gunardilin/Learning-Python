"""This code will test the nearest.py.
It is better but also a bad test code.
When something fails, the result is messy and it stops the program.
Ideally running a test should run all the unit tests and let you know which one 
failed and which one succeeded.
Try run the assert code with #"""
from nearest import nearest_square
 
nearest_5 = nearest_square(5)
print("Nearest square <= 5: returned {}, correct answer is 4.".format(nearest_5))
assert(nearest_5 == 4)
#assert nearest_5 == 14, "nearest_5 should be 4"

nearest_n12 = nearest_square(-12)
print("Nearest square <= -12: returned {}, correct answer is 0.".format(nearest_n12))
assert(nearest_n12 == 0)

nearest_9 = nearest_square(9)
print("Nearest square <= 9: returned {}, correct answer is 4.".format(nearest_9))
assert(nearest_9 == 9)

nearest_23 = nearest_square(23)
print("Nearest square <= 23: returned {}, correct answer is 4.".format(nearest_23))
assert(nearest_23 == 16)