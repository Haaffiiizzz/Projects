import schedule
from win10toast import ToastNotifier
from playsound import playsound
import time



def getScheduleInfo() -> list[dict]:
    print("Hello and welcome to this simple schedule maker!\n")
    time.sleep(1)

    allTasks = []
    addTask = True
    while addTask:
        task = {}
        task["taskName"] = input("What task do you want to add?:\n")
        time.sleep(1)
        task["taskFreq"] = input("What frequency do you want for this task? \
(Days, Hours, Minutes, Seconds, Once?):\n").upper()
        
        if task["taskFreq"][0] == "D":
            task["taskFreq"] = "day"
            haveExactTime = input("Do you have an exact day interval \
for this task?(Yes/No)").upper()
            time.sleep(0.5)
            if haveExactTime[0] == "Y":
                task["taskFreq"] = "days"
                task["exactTime"] = int(input("Type in the day interval you want:\n"))

        elif task["taskFreq"][0] == "H":
            task["taskFreq"] = "hours"
            haveExactInterval = input("Do you have an exact hour interval for this task?:\n").upper()
            time.sleep(0.5)
            if haveExactInterval[0] == "Y":
                task["exactTime"] = int(input("Type in the hour interval you want:\n"))

        elif task["taskFreq"][0] == "M":
            task["taskFreq"] = "minutes"
            haveExactInterval = input("Do you have an exact minutes interval for this task?:\n").upper()
            time.sleep(0.5)
            if haveExactInterval[0] == "Y":
                task["exactTime"] = int(input("Type in the minute interval you want:\n"))

        elif task["taskFreq"][0] == "S":
            task["taskFreq"] = "seconds"
            haveExactInterval = input("Do you have an exact seconds interval for this task?:\n").upper()
            time.sleep(0.5)
            if haveExactInterval[0] == "Y":
                task["exactTime"] = int(input("Type in the seconds interval you want:\n"))
        
        

        allTasks.append(task)
        time.sleep(1)
        addMoreTasks = input("Do you want to add anymore tasks? (Yes/No):\n").upper()
        if addMoreTasks[0] == "N":
            addTask = False

    return(allTasks)

def displaySchedule(task):
    message = ToastNotifier()
    name = task["taskName"]
    message.show_toast("Schedule", name, duration = 2, threaded = True)
    playsound("SIMPLE TIMER\Alarm beep.mp3", block = False)

def createSchedule(scheduleInfo: list):
    for event in scheduleInfo:
        exactTime = event.get("exactTime", 1)
        if event["taskFreq"] == "seconds":
            schedule.every(exactTime).seconds.do(displaySchedule, event)
        if event["taskFreq"] == "minutes":
            schedule.every(exactTime).minutes.do(displaySchedule, event)
        if event["taskFreq"] == "hours":
            schedule.every(exactTime).hours.do(displaySchedule, event)
        if event["taskFreq"] == "days":
            schedule.every(exactTime).days.do(displaySchedule, event)   

    while True:
        schedule.run_pending()
        time.sleep(1)
        
def main():
    scheduleInfo = getScheduleInfo()
    createSchedule(scheduleInfo)
if __name__ == "__main__":
    main()    
