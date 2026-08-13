from datetime import date, datetime

current_date = date.today()
user_input = input("Enter your goal with a deadline (DD.MM.YYYY) separated by a colon (e.g., 'Finish project:30')")
goal, deadline = user_input.split(":")
DD, MM, YYYY = deadline.split(".")
deadline_date = date(int(YYYY), int(MM), int(DD))

def days_calculation(deadline):
    if deadline_date < current_date:
        return -1
    else:
        remaining_days = (deadline_date - current_date).days
        return remaining_days

remaining_days = days_calculation(deadline_date)
if remaining_days != -1:
    print("Dear user! Time remaining for your goal: " , goal, "is", remaining_days, "days. Current date and time is:", current_date)
else:
    print("The deadline has already passed. Current date and time is:", current_date)