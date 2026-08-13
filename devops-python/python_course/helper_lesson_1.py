day_to_hours = 24
name_of_units = "hours"

def days_to_units(num_of_days, units):
    try:
        if units == "hours":
            print(f"{int(num_of_days)} days are {int(num_of_days) * day_to_hours} {units}")
        elif units == "minutes":
            print(f"{int(num_of_days)} days are {int(num_of_days) * day_to_hours * 60} {units}")
        elif units == "seconds":
            print(f"{int(num_of_days)} days are {int(num_of_days) * day_to_hours * 60 * 60} {units}")
        else:
            print("Invalid unit. Please enter 'hours', 'minutes', or 'seconds'.")
    except ValueError:
        print("Invalid input. Please enter a valid number of days and units.")

def days_to_hours(num_of_days):
    try:
        int(num_of_days)
        print(f"{int(num_of_days)} days are {int(num_of_days) * day_to_hours} {name_of_units}")
    except ValueError:
        print("Invalid input. Please enter a valid number of days.")


def validate_and_execute():
    try:
        user_input_number = int(input("Enter a number: "))
        if user_input_number > 0:
            days_to_hours(user_input_number)
        elif user_input_number == 0:
            print("You entered zero. Please enter a positive number.")
        else:
            print("You entered a negative number. Please enter a positive number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")