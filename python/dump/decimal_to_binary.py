# Convert deciaml to binary using successive division


number = 23
reminders = []
while number > 0:
    reminder = number % 2 
    number = number // 2
    reminders.insert(0, reminder)

result = "".join(str(r) for r in reminders)
print(f"{result:0>8}")



