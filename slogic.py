import csv

def importSBox(file):
    s_box = {}
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:       
            s_box[int(row[0])] = int(row[1])
    return s_box

def importSBox_asBinary(file):
    s_box = {}
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:       
            s_box[int(row[0],2)] = int(row[1],2)
    return s_box

               
def calculate_ddt(SBox_file: csv = 'SBox/SBox1.csv',delta_E_range: int = 32,delta_A_range: int = 32) -> list:
    ddt = [[[] for x in range(delta_A_range)] for y in range(delta_E_range)] #initialize 2d-Matrix with empty lists
    s_box = importSBox(SBox_file) 
    for a in range(delta_A_range):
        for e in range(delta_E_range):
            delta_E: int = a ^ e
            delta_A: int = s_box[a] ^ s_box[e]
            if delta_A > 0 and delta_E > 0:
                ddt[delta_A][delta_E].append((e,a))
    return ddt

def size_of_ddt(ddt: list[list[list]]) -> list[list[int]]:
    ddt_size = ([[0 for x in range(32)] for y in range(32)])
    for delta_A in range(1,32):
        for delta_E in range(1,32):
            ddt_size[delta_A][delta_E] = len(ddt[delta_A][delta_E])

    return ddt_size

def distribution_percentage(ddt: list[list[list]]) -> list[list[float]]:
    ddt_size_relative = size_of_ddt(ddt)
    for delta_A in range(32):
        for delta_E in range(32):
            ddt_size_relative[delta_A][delta_E] = float(ddt_size_relative[delta_A][delta_E]/32)
    return ddt_size_relative


