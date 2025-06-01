# Daily reminder App

Task = input("Enter you task")
Priority = input("Priority (high,medium,low)")
Time_bound = input("Is it time-bound?(yes/no): ")

match Priority:
    case 'high':
        if Time_bound == 'yes':
            print(f"Reminder: {Task} is a {Priority} task that requires immediate attention today!")
    case 'low':
        if Time_bound == 'no':
            print(f"Note: {Task} is a {Priority} priority task. Consider completing it when you have free time.")
    case _ :
        print("You didn't enter any task !")
