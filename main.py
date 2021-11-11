from slogic import calculate_ddt, importSBox, size_of_ddt
from krypto import encrypt
from linear import is_linear

s1 = importSBox('SBox/SBox1.csv')
#print(s1)

s2 = importSBox('SBox/SBox2.csv')
#print(s2)

s3 = importSBox('SBox/SBox11.csv')
#print(encrypt(s1, s2))

print(is_linear(s3))
ddt = calculate_ddt(SBox_file='SBox/SBox1.csv')
ddt_size = size_of_ddt(ddt)

for row in range(32):
    print(ddt_size[row])
