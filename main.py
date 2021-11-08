from slogic import calculate_ddt, importSBox
from krypto import encrypt

s1 = importSBox('SBox/SBox1.csv')
#print(s1)

s2 = importSBox('SBox/SBox2.csv')
#print(s2)

print(encrypt(s1, s2))

print(calculate_ddt())