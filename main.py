from slogic import calculate_ddt, distribution_percentage, importSBox, size_of_ddt
from slogic import calculate_ddt, importSBox, size_of_ddt
from output_ddt import test
from slogic import calculate_ddt, importSBox
from krypto import encrypt
from linear import is_not_linear, count_linear

s1 = importSBox('SBox/SBox1.csv')
print(is_not_linear(s1))
count_linear(s1)

s2 = importSBox('SBox/SBox2.csv')
print(is_not_linear(s2))
count_linear(s2)

s3 = importSBox('SBox/SBox3.csv')
#print(encrypt(s1, s2))


print(is_not_linear(s3))
count_linear(s3)

# print(is_not_linear(s1))
count_linear(s3)
ddt = calculate_ddt(SBox_file='SBox/SBox1.csv')
ddt_size = size_of_ddt(ddt)

#print(ddt)
test(ddt)

