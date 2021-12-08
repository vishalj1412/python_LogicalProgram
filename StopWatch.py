import time

def stopWatch():
 start=input("enter s to start the time  :  ")
 if(start=="s"):
  startTime=time.time()

 end=input(" enter e to end the time  :  ")
 if(end=="e"):
  endTime=time.time()

 elapsedTime=endTime - startTime

 print(elapsedTime)

stopWatch()