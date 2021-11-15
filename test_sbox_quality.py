import os

from slogic import calculate_ddt, size_of_ddt


def get_worst_sbox(myFolder = 'SBox'):
    fileset = [root+'/'+filename for root, _, files in os.walk(myFolder) for filename in files]

    #print(fileset)
    highest_differential_count: int = 0
    worst_sbox = []
    for file in fileset:
        #sbox = importSBox(file)
        sbox_ddt_size = size_of_ddt(calculate_ddt(file))
        for row in sbox_ddt_size:
            for differential_count in row:
                if differential_count >= highest_differential_count:
                    highest_differential_count = differential_count
                    worst_sbox.append((file,highest_differential_count))
    return worst_sbox

print(get_worst_sbox('SBox/Random_SBox'))