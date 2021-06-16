import csv
with open('d:/temp/students_2.csv', 'w', newline='') as csvfile:
    fields = ['id', 'name', 'phone', 'email']
    students = csv.DictWriter(csvfile, fieldnames=fields)
    #Write Header first before writing the actual data.
    students.writeheader()
    row = {'id': 1, 'name': 'A', 'phone': '23423432', 'email': 'abv@asdfas.com'}
    students.writerow(row)

    row = {'id': 2, 'name': 'B', 'phone': '4423432', 'email': 'DDD@asdfas.com'}
    students.writerow(row)
