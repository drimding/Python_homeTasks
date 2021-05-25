"""
File `data/students.csv` stores information about students in CSV format.
This file contains the student’s names, age and average mark.

1. Implement a function get_top_performers which receives file path and
returns names of top performer students.
Example:
def get_top_performers(file_path, number_of_top_students=5):
    pass

print(get_top_performers("students.csv"))

Result:
['Teresa Jones', 'Richard Snider', 'Jessica Dubose', 'Heather Garcia',
'Joseph Head']

2. Implement a function write_students_age_desc which receives the file path
with students info and writes CSV student information to the new file in
descending order of age.
Example:
def write_students_age_desc(file_path, output_file):
    pass

Content of the resulting file:
student name,age,average mark
Verdell Crawford,30,8.86
Brenda Silva,30,7.53
...
Lindsey Cummings,18,6.88
Raymond Soileau,18,7.27
"""
import csv
from operator import itemgetter


def get_top_performers(file_path: str, number_of_top_students=5):
    list_students = []
    with open(file_path) as csv_file:
        # wrapping a marker to the next line
        csv_file.readline()
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            list_students.append([row[0], int(row[1]), float(row[2])])
    # sorted list_students by average mark
    list_students = sorted(list_students, key=itemgetter(2), reverse=True)
    return [i[0] for i in list_students[:number_of_top_students]]


def write_students_age_desc(file_path: str, output_file: str):
    list_students = []
    first_line = []
    with open(file_path, "r") as input_file:
        # read first line and wrapping a marker to the next line
        first_line = input_file.readline().rstrip('\n').split(',')
        csv_reader = csv.reader(input_file)
        for row in csv_reader:
            list_students.append([row[0], int(row[1]), float(row[2])])
    # sorted list_students by students age
    list_students = sorted(list_students, key=itemgetter(1), reverse=True)
    with open(output_file, "w") as output_file:
        writer = csv.writer(output_file)
        # write first line
        writer.writerow(first_line)
        # write last sorted lines
        writer.writerows(list_students)
