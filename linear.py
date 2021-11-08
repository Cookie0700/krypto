# Nicht-linear = Nicht additiv/homogen
# 110  = S1(011) = S1(101 + 110) /= S1(101) + S1(110) = 111 + 101 = 010
# S1(00000) -> 

import csv

def linear_check(file):
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(row)
            # Input = {row[0]}
            # Output = {row[1]}

# linear_check('bits.csv')

def binary_combinations(bit_length): 
    for i in range(2**bit_length):
        s="{:05b}".format(i)
        print(s)
        
binary_combinations(5)

def test():
    a = '001'
    b = '011'
    c = int(a,2) + int(b,2)
    print(c)

# test()

# linear_check('SBox/SBox1.csv')