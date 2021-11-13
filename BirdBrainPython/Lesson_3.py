###Exercise1
bird.setBeak(100,0,0)
from BirdBrain import finch
from time import sleep 
bird = Finch()
Bird.setBeak(100,0,100)
sleep(1)
bird.setBeak(0,0,0)

##Exercise 2
bird.setBeak(100,0,100)
sleep(2)
bird.setBeak(0,100,100)
sleep(2)
bird.setBeak(100,100,0)

###Exercise 3
#The first light will be turned on and made blue then 
#the fourth light will be turned 
#on and made blue. Then the finch will wait 2 seconds and turn off all the lights

###Exercise 4 
bird.setBeak(100,0,0)
sleep(1)
bird.setBeak(100,30,0)
sleep(1)
bird.setBeak(100,100,0)
sleep(1)
bird.setBeak(0,100,0)
sleep(1)
bird.setBeak(0,0,100)
sleep(1)
bird.setBeak(100,0,100)

###Exercise 5
userResponse = input("Which tail light (1-4) should be red? ")
number = int(userResponse)
bird.setTail(number,100,0,0)
sleep(1)
bird.stopAll()

###Exercise 6 
userResponse = ("How much from (1-100) of red, green, and blue should there be")
number = int(userResponse)
bird.setTail(number,0,0,0)
sleep(3)
bird.stopAll()
