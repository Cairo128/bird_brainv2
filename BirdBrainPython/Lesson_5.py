#Exercise 1
if bird.getButton('A' or 'B'):
	bird.setBeak(0,100,0)
else:
	bird.setBeak(100,0,0)
sleep(1)
bird.stopAll()

#Exercie 2
if bird.getButton('B'):
	bird.setMove("B",25,100)
else:
	bird.setMove("F",30,100)
sleep(1)
bird.stopAll()

#Exercise 3 made a hypothesis for the code on the exercise

#Exercise 4
print(bird.getDistance())
if bird.getDistance() <30: 
	bird.setMove("B",5,100) 
else:
	bird.setMove("F",5,100)
sleep(2)
bird.stopAll()

print('Exercise 5')
while bird.getDistance() <30:
	bird.setBeak(100,0,0)
bird.setBeak(0,100,0)
sleep(1)

#Exercise 6
while bird.getDistance() > 15:
	bird.setMotors(50,50)

bird.stopAll
