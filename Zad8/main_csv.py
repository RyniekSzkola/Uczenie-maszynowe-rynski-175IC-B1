import csv
import pandas as pd

#Otworzenie pliku csv i zapisanie go do pamięci
with open('employee_birthday.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    #Pętla zliczająca wszystkie wiersze oraz wypisująca dane
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are: {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')

#Tworzenie plików csv
with open('employee_file.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    employee_writer.writerow(['Name', 'LastName', 'Age'])
    employee_writer.writerow(['Erica', 'Meyes', '23'])
    employee_writer.writerow(['Michal', 'Rynski', '22'])
    employee_writer.writerow(['Adam', 'Nowak', '29'])

#Inny sposob tworzenia plikow csv
with open('employee_file2.csv', mode='w') as csv_file:
    fieldnames = ['Name', 'LastName', 'Age']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'Name': 'John', 'LastName': 'Smith', 'Age': '34'})
    writer.writerow({'Name': 'Erica', 'LastName': 'Meyers', 'Age': '29'})

#Wczytywanie plikow do pamięci za pomocą biblioteki pandas
df = pd.read_csv('addresses.csv')
print(df)