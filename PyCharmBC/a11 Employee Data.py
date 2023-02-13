import os


def adEmpl():
    whEmpl = input("Which employee must be added? Bob, Kim, or Sam?")
    if whEmpl == "Bob":
        f = open("a11.txt", "a")
        emp = 'Bob', 'salary ' '$100,000', 'job ' 'Mgr'
        emp = str(emp)
        f.write("\n" + emp + "\n")
        print("Bob had been added!")
    elif whEmpl == "Kim":
        f = open("a11.txt", "a")
        emp = 'Kim', 'salary ' '$100,000', 'job ' 'Dev'
        emp = str(emp)
        f.write("\n" + emp + "\n")
        print("Kim has been added!")
    elif whEmpl == "Sam":
        f = open("a11.txt", "a")
        emp = 'Sam', 'salary ' '$100,000', 'job ' 'Dev'
        emp = str(emp)
        f.write("\n" + emp + "\n")
        print("Sam has been added!")
    else:
        print("Not found")

while (True):
    reAdd = input("Do you need to add an employee? y for yes")

    if reAdd == "y":
        adEmpl()
    else:
        print("Not valid")

    again = input("Need more adjustments?")
    if again != "y":
        break