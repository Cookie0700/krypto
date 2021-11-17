from krypto import single_round_encrypt
from slogic import importSBox



def differential_encryption_analysis(difference: int) -> list: #engine for differential encryption
    s1 = importSBox('SBox/Random_SBox/151.csv')
    s2 = importSBox('SBox/Random_SBox/940.csv')
    four_round_input_pairs: list = []
    for a in range(1024):
        for b in range(1024):
            if (a ^ b) == difference:
                four_round_pairs: list = [(a,b)]
                for _ in range(4):
                    a = single_round_encrypt(s1, s2, a)
                    b = single_round_encrypt(s1, s2, b)
                    four_round_pairs.append((a,b))
                four_round_input_pairs.append(four_round_pairs)

    return four_round_input_pairs


def binary_difference(input_tuple: tuple) -> int:
    (a,b) = input_tuple
    return a ^ b

def calculate_characteristics(input_difference: int) -> list[dict]:
    pair_list = differential_encryption_analysis(input_difference)
    characteristics = []
    for four_round_pairs in pair_list:
        characteristic = {}
        characteristic['D0'] = binary_difference(four_round_pairs[0])
        characteristic['D1'] = binary_difference(four_round_pairs[1])
        characteristic['D2'] = binary_difference(four_round_pairs[2])
        characteristic['D3'] = binary_difference(four_round_pairs[3])
        characteristic['D4'] = binary_difference(four_round_pairs[4])
        characteristics.append(characteristic)
    return characteristics

#print(calculate_characteristics(1))
            
def significant_characteristic(input_difference: int) -> list:
    characteristics = calculate_characteristics(input_difference)
    rminus1_diff = []
    for characteristic in characteristics:
        rminus1_diff.append(characteristic['D4'])
    return rminus1_diff

#print(significant_characteristic(1))

def stat_of_rminus1_diff(rminus1_diff: list) -> dict:
    stats = dict((i, rminus1_diff.count(i)) for i in rminus1_diff)
    return stats


rminus1_diff = significant_characteristic(1)
print(stat_of_rminus1_diff(rminus1_diff))

    






                

