from krypto import single_round_encrypt
from slogic import importSBox

s1 = importSBox('SBox/SBox1.csv')
s2 = importSBox('SBox/SBox2.csv')

def differential_encryption(difference: int) -> list: #engine for differential encryption
    
    for a in range(1024):
        for b in range(1024):
            if (a ^ b) == difference:
                for _ in range(4):
                    a = single_round_encrypt(s1, s2, a)
                    b = single_round_encrypt(s1, s2, b)
                



                

