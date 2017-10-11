import math
sideA = input("What is the length of Side A: ")
sideB = input("What is the length of Side B: ")
sideC = (sideA * sideA) + (sideB * sideB)
sideC = math.sqrt(sideC)
print "The length of Side C is {}".format(sideC)
