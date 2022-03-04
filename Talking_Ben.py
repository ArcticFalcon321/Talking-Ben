#Import time for time.sleep and random for random option
import time
import random
#Calling Ben
print("Ring, Ring")
time.sleep(1)
#Ben picks up the phone
print("Ben?")
#While true so infinity ben
while True:
    #input Ask ben so the user can ask anything
    input("Ask Ben:")
    print(''.join(random.sample(('No', 'Yes', 'Hohoho', 'Ouh'), 1)))