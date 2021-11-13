bird.setMotors(50,50)
sleep(1)
bird.stop()
#Exercise 1 
#Speeds that are equal and opposite (50 and -50, for example) make
# the Finch turn in place.

# Exercise 2 the user enters the speeds of the left and right wheels.
# As the two speeds get closer together, the radius of the turn gets larger

# Exercise 3
userResponse = input("5 seconds")
time = float(userResponse)
bird.setMotors(100,0)                      
sleep(1)
bird.stop()

#Exercise 4
#We don't need to convert color to another type because it is already a string