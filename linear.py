import csv
# 110  = S1(011) = S1(101 + 110) /= S1(101) + S1(110) = 111 + 101 = 010

def is_linear(sbox): 
    for i in range(32):
        for j in range(32): 
            # print(i ^ j)
            if sbox[i ^ j] == (sbox[i] ^ sbox[j]):
                print(i, j)
                return True
    return False