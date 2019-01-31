import os ,csv


def main():
    filename = input("Enter file name")
    read_and_create_new_csv(filename)


def read_and_create_new_csv(filename):
    os.makedirs('formatted', exist_ok=True)
    file = open(filename)
    csv_file = csv.reader(file)
    array_file = list(csv_file)
    new_csv = format_array(array_file)
    new_csv_file = open(os.path.join('formatted', filename), 'w', newline='')
    writer = csv.writer(new_csv_file)

    for row in new_csv:
        writer.writerow(row)

    new_csv_file.close()


def format_array(array_file):

    row = len(array_file)
    col = len(array_file[0])
    col_delimiter = [0, 2, 3]
    boolean_cols = [5, 6, 16]
    new_row = []
    new_csv = []

    for i in range(row):
        for j in range(col):

            if j > 1:
                if not j in col_delimiter:
                    if j >= 17 and j <= 41 and array_file[i][j] == 1:
                        new_row.append(array_file[i][0])

                    elif j in boolean_cols:
                        if array_file[i][j] == 1:
                            new_row.append('Yes')
                        else:
                            new_row.append('No')
                    elif j == 13:
                        new_row.append(non_student(array_file[i][j]))

                    elif j == 14:
                        new_row.append(academic_level(array_file[i][j]))

                    else:
                        new_row.append(array_file[i][j])

        new_csv.append(new_row)
        new_row = []

    return new_csv


def academic_level(array_item):
    switcher = {
        1: "Freshman",
        2: "Sophmore",
        3: "Junior",
        4: "Senior",
        5: "Graduate/Professional",
        6: "Non-Degree",
        7: "Faculty/Staff"
    }.get(array_item, " ")


def non_student(array_item):
    switcher = {
        1: "High School",
        2: "Transfer",
        3: "Communty Member"

    }.get(array_item, " ")


if __name__ == "__main__":
    main()