# Daily reminder App

user = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case 'high':
        if time_bound == 'yes':
            print(f"Reminder: {user} is a {priority} task that requires immediate attention today!")
    case 'low':
        if time_bound == 'no':
            print(f"Note: {user} is a {priority} priority task. Consider completing it when you have free time.")
    case _ :
        print("You didn't enter any task !")
