# Ben Rongey
# Builds a graphical tree of PID's, PPID's, and Levels of those PID's

import csv
from graphviz import Digraph

with open("forkOutput.csv") as my_file:
    
    dot = Digraph()
    csv_reader = csv.reader(my_file, delimiter=',')
    line_count = 0

    for row in csv_reader:
        id_number = str.strip(row[0])
        parent_id = str.strip(row[1])
        level_num = str.strip(row[2])
        fork_of = str.strip(row[3])

        if line_count == 0:
            line_count = line_count + 1

        elif line_count == 1:
            dot.node(id_number, 'PID: ' + id_number + '\n' + 'Level: ' + level_num)
            line_count = line_count + 1

        else:
            dot.node(id_number, 'PID: ' + id_number + '\n' + 'Level: ' + level_num)
            dot.edge(fork_of, id_number)
            line_count = line_count + 1

    dot.render('tree-graph.gv', view=True)

my_file.close()