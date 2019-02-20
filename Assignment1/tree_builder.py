# Ben Rongey
# Builds a graphical tree of PID's, PPID's, and Levels of those PID's

import csv

with open("forkOutput.csv") as my_file:
    
    csv_reader = csv.reader(my_file, delimiter=',')
    line_count = 0

    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {",".join(row)}')
            line_count = line_count + 1

        else:
            print(f'PID is {row[0]} and PPID is {row[1]} and level is {row[2]}')
            line_count = line_count + 1
    
    print()
    print()
    print(f'Processed {line_count} lines.')

my_file.close()