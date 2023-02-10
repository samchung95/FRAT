import csv
import os
from datetime import datetime

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
            csvfile.close()

    with open(csvpath, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)

        writer.writeheader()
        writer.writerows(data)
        csvfile.close()

def writeNewAttendance(data:list[dict]):

    today = datetime.now().date()
    today_set = set()

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

                row_date = datetime.strptime(row[header[1]], '%d/%m/%y').date()
                
                print(row_date, today)

                if row_date == today:
                    today_set.add(row[header[0]])

            data = [d for d in data if d[list(d.keys())[0]] not in today_set]
            print(data)
            data=temp+data

    with open(csvpath, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)

        writer.writeheader()
        writer.writerows(data)


if __name__ == "__main__":
    d = datetime.now().strftime('%d/%m/%y')
    writeNewAttendance([{'name':'huai','date':d}])
    pass