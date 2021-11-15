from krypto import single_round_encrypt
from slogic import importSBox



def differential_encryption_analysis(difference: int) -> list: #engine for differential encryption
    s1 = importSBox('SBox/Random_SBox/151.csv')
    s2 = importSBox('SBox/Random_SBox/940.csv')
    characteristics: list = []
    for a in range(1024):
        for b in range(1024):
            if (a ^ b) == difference:
                four_round_characteristic: list = [(a,b)]
                for _ in range(4):
                    a = single_round_encrypt(s1, s2, a)
                    b = single_round_encrypt(s1, s2, b)
                    four_round_characteristic.append((a,b))
                characteristics.append(four_round_characteristic)

    return characteristics
print(differential_encryption_analysis(1))
                



                

