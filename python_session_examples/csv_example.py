import csv

with open('d:/temp/students.csv') as student_file:
    student_reader = csv.DictReader(student_file)
    for row in student_reader:
        if row.get('column_name') == 'value':
