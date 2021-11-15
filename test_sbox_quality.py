import os

from slogic import importSBox, calculate_ddt, size_of_ddt


def get_worst_sbox(myFolder = 'SBox'):
    fileset = [root+'/'+filename for root, _, files in os.walk(myFolder) for filename in files]

    print(fileset)
    highest_differential_count: int = 0
    worst_sbox: str 
    for file in fileset:
        #sbox = importSBox(file)
        sbox_ddt_size = size_of_ddt(calculate_ddt(file))
        for row in sbox_ddt_size:
            for differential_count in row:
                if differential_count > highest_differential_count:
                    highest_differential_count = differential_count
                    worst_sbox = file
    return worst_sbox, highest_differential_count

print(get_worst_sbox())