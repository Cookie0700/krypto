import csv

def importSBox(file):
    s_box = {}
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:       
            s_box[int(row[0],2)] = int(row[1],2)
    return s_box

               
def calculate_ddt(SBox_file: csv = 'SBox/SBox1.csv',delta_E_range: int = 32,delta_A_range: int = 32) -> list:
    ddt = [[[] for x in range(delta_A_range)] for y in range(delta_E_range)]
    s_box = importSBox(SBox_file)
    for a in range(delta_A_range):
        for e in range(delta_E_range):
            delta_E: int = a ^ e
            delta_A: int = s_box[a] ^ s_box[e]
            ddt[delta_A][delta_E].append((e,a))
    return ddt

