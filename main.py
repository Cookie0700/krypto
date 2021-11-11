from slogic import calculate_ddt, importSBox, size_of_ddt
from krypto import encrypt

s1 = importSBox('SBox/SBox1.csv')
#print(s1)

s2 = importSBox('SBox/SBox2.csv')
#print(s2)

#print(encrypt(s1, s2))

ddt = calculate_ddt(SBox_file='SBox/SBox1.csv')
ddt_size = size_of_ddt(ddt)

for row in range(32):
    print(ddt_size[row])
