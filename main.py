from output_ddt import csv_print
#from output_ddt import test2
from slogic import calculate_ddt, importSBox
from krypto import encrypt

s1 = importSBox('SBox/SBox1.csv')
#print(s1)

s2 = importSBox('SBox/SBox2.csv')
#print(s2)

print(encrypt(s1, s2))

print(calculate_ddt())

print("\n\n")

ddt = calculate_ddt()
csv_print(ddt)
#test2(ddt)