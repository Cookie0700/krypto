import csv

s1 = {}

def importSBox(file):
    s = {}
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            #print(f'Input: {row[0]}, Output: {row[1]}')         
            s[int(row[0],2)] = int(row[1],2)
    return s


#importSBox()
#print(s1)
               
