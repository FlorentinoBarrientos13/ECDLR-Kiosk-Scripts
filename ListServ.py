import os
import csv

def main():
    filename = input("Enter file name\n")
    file = open(filename)
    read = csv.reader(file)
    arr = list(read)
    row = len(arr)
    listServ_col = 16
    serv = open("listserv.txt", "w")
  #Check whether the student chose yes to signup for the listserv
    for rows in range(row):
        if len(arr[rows][listServ_col]) > 0 and arr[rows][listServ_col] == '1' :
            serv.write(arr[rows][listServ_col] + ",")
    serv.close()

if __name__ == "__main__":
  main()
pass
