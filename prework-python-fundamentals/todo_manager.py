print("=" * 50)
print(" " * 15 + "My To-DO List" + " " * 15)
print("=" * 50)

tasks = ["Get gas", "Practice coding", "Make food"]

for task in tasks:
    print(f"{tasks.index(task)+1}.  {task}")

print("\nTotal tasks:  ", len(tasks))

while True: #in order to keep asking for input until valid input is given
    print("\nWhat would you like to do? \n1. Add a task " \
    "\n2. Remove a task")
    task_choice = input("> ")

    try:
        if task_choice == "1": #if user chooses to add a task
            print(f"\nChoice: {task_choice}")
            new_task = input("Enter new task: ")
            tasks.append(new_task)
            print(f"Task '{new_task}' added to the list.")

        elif task_choice == "2": #if user chooses to remove a task
            print(f"Choice: {task_choice}")
            remove_task = input("Enter task to remove: ")

            try:
                remove_task_int = int(remove_task) - 1 #converts user input to an integer and subtracts 1 to match the index of the list

                if remove_task_int < len(tasks) and remove_task_int >= 0: #checks if the input is a valid index in the list
                    removed_task = tasks.pop(remove_task_int) #removes the task at the index of the user input
                    print(f"Task '{removed_task}' removed from the list.")
                else:
                    raise ValueError("Please enter a valid task number.") #ensures the user puts a valid number from the list

            except ValueError:
                raise ValueError("Please enter a number using digits greater than 0, and shown on the list above.") #catches ValueError if input is not valid, then continues the While loop

        else:
            raise ValueError("Please enter 1 or 2.") #catches ValueError if input is not valid, then continues the While loop

        break #breaks while loop if input is valid

    except ValueError as v: #raised value errors come here
        print(f"Error: {v}")

print("\nUpdated list:") #prints updated list of tasks after user input

for task in tasks:
    print(f"{tasks.index(task)+1}.  {task}")

print("Total tasks:  ", len(tasks)) #final total number of tasks after user input

