"""
TASK 2
Write a program to get "HIRE DATE" of employee who's department is within range 30
to 110 AND who's salary is > 4200.
The output should be in following format.

{
"<HIRE DATE in YYYY-MM-DD format>": [
"<first_name last_name>",
...,
"<first_name last_name>"
],
}
"""
import csv

with open("employees.csv", "r") as f:
    reader = csv.DictReader(f)
    employees = list(reader)
    # print(employees)
for emp in employees:
    for key, value in emp.items():
        if key == "DEPARTMENT_ID":
            value = int(value)
            if 30 < int(emp["DEPARTMENT_ID"]) <=110 and int(emp["SALARY"]) > 4200:
                print(f"HIRE DATE :{emp['HIRE_DATE']} \nDEPT_ID :{emp['DEPARTMENT_ID']} \nNAME:{emp['FIRST_NAME']} "
                      f"{emp['LAST_NAME']}\nSALARY :{emp['SALARY']}\n")
