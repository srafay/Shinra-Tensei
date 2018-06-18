# Reading from a csv file

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

    def testInstance(self):
        return [self.name, self.code, self.year, self.credit]


filename = input("Enter the name of the file: ")
Data = []

with open(filename, 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        Data.append(row)

courses = [Course() for _ in range(len(Data))]

for i in range(len(Data)):
    courses[i].Initialize(Data[i].get('name'), Data[i].get('code'), Data[i].get('year'), Data[i].get('credit'))
    print(courses[i].testInstance())


