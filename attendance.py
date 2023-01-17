import csv

def csvToDict(filepath):
    dic = {}
    with open(filepath,'r') as file:
        lines = file.readlines()
        header_row = lines[0]
        headers = header_row.split(',')
        rows = lines[1:]

        for row in rows:
            columns = row.split(',')
            dic[columns[0]] = {}
            for i,header in enumerate(headers):
                dic[columns[0]][header] = columns[i]

        file.close()

    return dic
        #TRUNCATE


with open('attendance.csv', mode='r') as infile:
    reader = csv.reader(infile)
    with open('coors_new.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        mydict = {rows[0]:rows[1] for rows in reader}