from BirdBrain import Finch
bird = Finch()

#Exercise 1

#Checks the finch's distance from the finch to the water bottle
#Distance 30cm

# print("Distance: ", bird.getDistance())
"""
#Exercise 2
print("RightLight: ", bird.getLight("R"))
print("LeftLight: ", bird.getLight("L"))
print("ButtonA: ", bird.getButton("A"))
print("Orientation: ", bird.getOrientation())
bird.setMove("F",10,50)
print("Encoder: ", bird.getEncoder("R"))
"""
currentDistance = bird.getDistance()
print(currentDistance)
print(2*currentDistance)
print(4*currentDistance)
