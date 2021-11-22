import datetime




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

for routine in routines:
    print(routine)


wakeup_str = input("Enter wake up time: ")
h, m = wakeup_str.split(':')
wakeup_timedelta = datetime.timedelta(hours=int(h), minutes=int(m))

#print(wakeup_timedelta)
timedelta = datetime.timedelta()

print(wakeup_str, "Wake up")
for title, duration in routines:
    print(wakeup_timedelta, title)
    td = datetime.timedelta(minutes=duration)
    wakeup_timedelta += td




