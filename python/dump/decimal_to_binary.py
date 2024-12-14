# Convert deciaml to binary using successive division


number = 107000
reminders = []
while number > 0:
    reminder = number % 2 
    number = number // 2
    reminders.append(reminder)

result = "_".join(str(r) for r in reminders)
print(f"{result:0>16}")



