import csv
# 110  = S1(011) = S1(101 + 110) /= S1(101) + S1(110) = 111 + 101 = 010

def is_not_linear(sbox): 
    for i in range(32):
        for j in range(32): 
            # print(i ^ j)
            if sbox[i ^ j] != (sbox[i] ^ sbox[j]):
                return True
    return False

def count_linear(sbox):
    linear_count = []
    linear_counter = 0 
    for i in range(32):
        for j in range(32): 
            if sbox[i ^ j] == (sbox[i] ^ sbox[j]):
                linear_count.append((i, j))
                linear_counter += 1
    print("Linear Counter: ", linear_counter)
    print("Linear Counter List: ", linear_count)
