task =[]

def addTask():
    task = input("please enter a task")
    task.append(task)
    print(f"task '{task}' added to the list")

    

def listTasks():
    if not tasks:
        print("there are no tasks currently")
    else:
        print("current tasks")
        for index, task in enumerate(tasks):
            print(f"task #{index}. {task}")

def deleteTask():
    listTask()
    try:
        taskToDelete = int(input("choose the # of the task you want to delete"))
        if taskToDelete >=0 and taskToDelete < len(tasks):
            Tasks.pop(taskToDelete)
            print(f"{taskToDelete} has been removed")
        
        else:
            print(f"{taskToDelete} was not found")
    except:
        print("invalid input")
     
    print(f"task '{task}' added to the list")

if __name__ =="__main__":
    print("Welcome to the to do list app :")
    while True:
        print("\n")
        print("please seleact the following options:")
        print("____________")
        print("1. Add a new task:")
        print("2.Delete a new task")
        print("3. list tasks")
        print("4.Quit")

        choice = input("enter your choice:")

        if(choice == "1"):
            addTask()

        elif(choice == "2"):
            deleteTask()

        elif(choice == "3"):
            listTask()

        elif(choice == "4"):
            break
        else:
            print("invalid input please try again")

print("goodbye")