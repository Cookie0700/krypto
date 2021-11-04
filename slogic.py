import csv

def importSBox(file):
    s_box = {}
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:       
            s_box[int(row[0],2)] = int(row[1],2)
    return s_box

               
