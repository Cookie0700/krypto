from output_ddt import csv_print
from slogic import calculate_ddt, importSBox, distribution_percentage, size_of_ddt
from krypto import encrypt
from linear import is_not_linear, count_linear

# s1 = importSBox('SBox/SBox1.csv')
# print(is_not_linear(s1))
# count_linear(s1)

# s2 = importSBox('SBox/SBox2.csv')
# print(is_not_linear(s2))
# count_linear(s2)

s3 = importSBox('SBox/Random_SBox/151.csv')
print(is_not_linear(s3))
count_linear(s3)

ddt = calculate_ddt(SBox_file='SBox/Random_SBox/151.csv')
ddt_size = size_of_ddt(ddt)

csv_print(ddt)

