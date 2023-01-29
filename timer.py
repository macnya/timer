import time

#Defining the timer
def setTimer():
    print("Please enter the time you want to set the timer.")
    timerHours = int(input("Hours: "))
    timerMinutes = int(input("Minutes: "))
    timerSeconds = int(input("Seconds: "))

    #Calculating the total time in seconds
    totalTime = (timerHours * 3600) + (timerMinutes * 60) + timerSeconds

    print("Timer set for " + str(timerHours) + " hours, " + str(timerMinutes) + " minutes, and " + str(timerSeconds) + " seconds.")

    #Looping until the timer is done
    while totalTime >= 0:
        print(str(totalTime) + " seconds remaining...")
        time.sleep(1)
        totalTime -= 1

    print("Time is up!")

#Calling the timer
setTimer()
