# Writing to a csv file

import csv

class Course:

    totalCourses = 0

    def __init__(self):
        Course.totalCourses += 1

    def Initialize(self, name, code, year, credit):
        self.name = name
        self.code = code
        self.year = year
        self.credit = credit

# Some temp vars
name = code = year = ""
credit = 0

numberOfCourses = int(input("Enter number of courses: "))

# List of instances
courses = [Course() for _ in range(numberOfCourses)]

for i in range(numberOfCourses):
    name = input("Enter the name of course: ")
    code = input("Enter the code of course: ")
    year = input("Enter the year of course: ")
    credit = int(input("Enter the credits of course: "))
    courses[i].Initialize(name, code, year, credit)

filename = input("Enter the name of file to store: ")

# Windows interprets \r\n to \r\r\n
# so you get blank lines between each row
# thus you need newline='' option for windows

with open(filename, 'w', newline='') as csvfile:

    fieldnames = ['name', 'code', 'year', 'credit']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write Header of csv once
    writer.writeheader()
    
    for i in range(Course.totalCourses):
        jsonData = {'name': courses[i].name,
                    'code': courses[i].code,
                    'year': courses[i].year,
                    'credit': courses[i].credit,
            }
        # Using DictWriter for writing in csv since we have data in JSON
        writer.writerow(jsonData)
        
    print("Writing complete")
