import datetime

# Bring emojies
# put zero before single digit hour
# Fix pass mindnight; not a day.
# Add habits part.


class Routine:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
        self.status = ""

# (title, duration)
routines = [("Exercise", 15),("Shower", 15),
            ("Meal 0", 30), ("Career 1", 60),
            ("Career 2", 60), ("Career 3", 60),
            ("Walk", 30), ("Career 4", 60),
            ("Career 5", 60), ("Career 6", 60),
            ("Read article", 30), ("Lunch", 30),
            ("Nap", 30), ("Business 1", 60),
            ("Business 2", 60), ("English", 30),
            ("Business 3", 60), ("Business 4", 60),
            ("Math", 30), ("Dinner", 30),
            ("CS 1", 60), ("CS 2", 60),
            ("Read book", 30), ("Japaneses", 30),
            ("Yoga", 15)
    ]


wakeup_str = input("Enter wake up time: ")
time_format = "%H:%M"
next_routine = datetime.datetime.strptime(wakeup_str, time_format)

for title, duration in routines:
    output = "{:%H:%M} {}".format(next_routine, title) 
    print(output)
    next_routine = next_routine + datetime.timedelta(minutes=duration)
