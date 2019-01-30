import csv, os

def read_and_create_new_csv(filename):
    file  = open(filename)
    csv_file = csv.reader(file)
    array_file = list(csv_file)


def format_string(array_file):
    row = len(array_file)
    col_delimiter  = [1 ,3, 4]

    for i in row:

        for j in col:
            if not j in col_delimiter:
                new_row.append(array_file[i][j])
                csv.write

        new_row = []        


    
    