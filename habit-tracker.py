from datetime import datetime, timedelta

# Thanks for checking out my code, I hope this really helps
habits = []


class Habit: 
    def __init__(self, name):
        self.name = name
        self.DATE_CREATION = datetime.today().date()
        self.streak = 0
        self.total_days = 0 # This is the total amount days available to do the habit
        self.total_completed = 0 # This is how many times you have completed the habit

    def get_habit_percentage(self):
        return self.total_completed / self.total_days


def create_habit(habit_list):
    habit_name = input("Please enter the name of your habit: ")
    created_habit = Habit(habit_name)
    habit_list.append(created_habit)

def log_habit(habit):
    current_date = datetime.today().date()

    difference = current_date - habit.DATE_CREATION
    print(difference.days)

    habit.streak += 1
    habit.total_completed += 1
    print("Congratulations on completing the habit!")



create_habit(habits)

log_habit(habits[0])