import os,csv

## inits the program
def main():
    filename = input("Enter file name")
    read_and_create_new_csv(filename)
    print("File made. Check the folder name formatted for your new file")


##Takes the csv file, formats it and creates a new directory containing the KioskSignInsFormatted file
def read_and_create_new_csv(filename):
    os.makedirs('KioskSignInsFormatted', exist_ok=True)
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
    #we dont want the students completed date/language/ entry number
    col_delimiter = [0, 2, 3]
    boolean_cols = [4, 5, 16]
    new_row = []
    new_csv = []
    reason_string = ""

    for i in range(row):
        for j in range(col):
            #if its not the header, do not format it
            if i > 0:
                if not j in col_delimiter:
                    #format the non_student entries
                    if j == 13:
                        new_row.append(non_student(array_file[i][j]))
                    #format the academic level of the students
                    elif j == 14:
                        new_row.append(academic_level(array_file[i][j]))
                    #collect students reasons for visiting
                    elif 16 < j < 43:
                        if array_file[i][j] == '1':
                            reason_string += array_file[0][j]
                    #format the yes/no questions
                    elif j in boolean_cols:

                        if array_file[i][j] == '1':
                            new_row.append('Yes')
                        elif array_file[i][j] == '2':
                            new_row.append('No')
                        else:
                            new_row.append(' ')
                    elif j == 43 or j == 44:
                        reason_string += array_file[i][j]

                    else:
                        new_row.append(array_file[i][j])
            #Create the header with original names until the 18 column. make the 18th column and name it reasons
            else:
                if j < 17:
                    if not j in col_delimiter:
                        new_row.append(array_file[i][j])
                elif j == 17:
                    new_row.append("Reason")
        #creates 2d array containing the new rows
        new_row.append(reason_string)
        new_csv.append(new_row)
        #reset the strings and rows for the upcoming row
        reason_string = ""
        new_row = []

    return new_csv

#formats the given acadamic lvl of a student
def academic_level(array_item):
    switcher = {
        '1': "Freshman",
        '2': "Sophmore",
        '3': "Junior",
        '4': "Senior",
        '5': "Graduate/Professional",
        '6': "Non-Degree",
        '7': "Faculty/Staff"
    }
    return switcher.get(array_item, " ")

#If it is a non student, return the string representing the 
def non_student(array_item):
    switcher = {
        '1': "High School",
        '2': "Transfer",
        '3': "Communty Member"

    }
    return switcher.get(array_item, " ")


if __name__ == "__main__":
    main()
