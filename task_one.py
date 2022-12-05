"""
TASK 1:
Write a program to get details of employees who's salary is > 9000. The output should
be in following format
"""
import csv


with open('employees.csv', 'r') as f:
    reader = csv.DictReader(f)
    employees = list(reader)
for emp in employees:
    for key, value in emp.items():
        if key == 'SALARY':
            value = int(value)
            if value > 9000:
                new_output = (F"Name: {emp['FIRST_NAME']} {emp['LAST_NAME']}\nemail:{emp['EMAIL']}\nphone number : "
                             F"{emp['PHONE_NUMBER']} \n")
                print(new_output)
