import csv
import os

def writeAttendance(data:list[dict]):

    header = list(data[0].keys())

    dir_path = os.path.dirname(os.path.realpath(__file__))
    csvpath = os.path.join(dir_path,'attendance.csv')

    if os.path.exists(csvpath):
        with open(csvpath, newline='') as csvfile:

            reader = csv.DictReader(csvfile)
            temp = []
            for row in reader:
                r = {header[0]: row[header[0]],
                     header[1]: row[header[1]]}
                temp.append(r)

            data=temp+data

    with open(csvpath, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)

        writer.writeheader()
        writer.writerows(data)



if __name__ == "__main__":
    # writeAttendance([{'name':'Huai','date':'test8'}])
    pass