import helper_lesson_1 as helper #from helper_lesson_1 import * (called all functions and variables from helper_lesson_1.py)
from helper_lesson_1 import days_to_hours
import os

print(os.name)
print("Current working directory:", os.getcwd())


days_to_hours("gnf")
days_to_hours(10)
helper.validate_and_execute()


user_input = "exit"
while user_input != "exit":
    user_input = input("Enter a number of days to convert to hours (or type 'exit' to quit): ")
    if user_input.lower() == "exit":
        print("Exiting the program.")
        break
    else:
        for i in user_input.split(","):
            days_to_hours(i)

#months of the year
months = ["January", "February", "March", "April", "May", "June",]
print(months[0])
months.append("July")
print(months)
months.remove("February")
print(months)
months.insert(1, "February")
print(months)
months.pop(2)
print(months)
months.sort()
print(months)
months.reverse()
print(months)      
months.clear()
print(months)

set_input = "exit"
while set_input != "exit":
    set_input = input("Enter a number of days to convert to hours (or type 'exit' to quit): ")
    if set_input.lower() == "exit":
        print("Exiting the program.")
        break
    else:
        print(set(set_input.split(",")))
        set(set_input.split(",")).copy()
        for i in set(set_input.split(",")):
            days_to_hours(i)

days_and_unit_input = ""
while days_and_unit_input != "exit":
    days_and_unit_input = input("Enter a number of days and conversion units (or type 'exit' to quit): ")
    if days_and_unit_input.lower() == "exit":
        print("Exiting the program.")
        break
    else:
        days_and_unit = days_and_unit_input.split(":")
        days_and_unit_dict = {"days" : days_and_unit[0], "units" : days_and_unit[1]}
        print(days_and_unit_dict)
        helper.days_to_units(days_and_unit_dict["days"], days_and_unit_dict["units"])


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


person1 = Person("Alice", 30)
person1.greet()

person2 = Person("Bob", 25)
person2.greet()