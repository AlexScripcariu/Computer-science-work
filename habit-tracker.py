from datetime import datetime
import json


class Habit:
    def __init__(self, habit):
        self.habit = habit
        self.streak = 0
        self.last_logged = datetime(2025, 1, 14).date()

        # load data if the file exists, otherwise save initial data
        try:
            self.load_data()
        except FileNotFoundError:
            self.save_data()

    def save_data(self):
        with open("habit_stats.json", "w") as file:
            json.dump(
                {**vars(self), "last_logged": str(self.last_logged)},
                file,
                indent=4
            )

    def load_data(self):
        with open("habit_stats.json", "r") as file:
            data = json.load(file)
            self.__dict__.update(
                {key: datetime.strptime(value, "%Y-%m-%d").date() if key == "last_logged" else value
                 for key, value in data.items()}
            )

    def log(self):
        current_date = datetime.today().date()
        if self.last_logged == current_date:
            print("You have already logged your habit today!")
            return

        if input("Press Enter to confirm the log, 'n' to cancel: ") == 'n':
            return

        self.streak = self.streak + 1 if (current_date - self.last_logged).days == 1 else 1
        self.last_logged = current_date
        self.save_data()
        print(f"Successfully logged! '{self.habit}' Streak: {self.streak}")
