#Create an empty list
Task_List = []

beginning = """Insert the number corresponding to the action you want to perform:
1. insert a new task;
2. remove a task;
3. show all the tasks;
4. close the program.
Your choice: """

print(beginning)

choice=0

#Select an option
while choice != 4:
    choice=int(input())
    if choice == 1:
        print("Insert a new task: ")
        new_task = input()
        Task_List.append(new_task)
    elif choice == 2:
        print("Insert a task to remove: ")
        to_remove = input()
        if Task_List.__contains__(to_remove):
            Task_List.remove(to_remove)
    elif choice == 3:
        print("Printing the whole list: ")
        print(Task_List)
    else:
        print("Starting again...")


