import csv
#inputs der funktion
sbox_size = 5

a = bin(32)

headerlist = [" "]
rows = []
for i in range (2**sbox_size):
    headerlist.append(i) 

for j in range(32):
    dic = {" " : j}
    for k in range (2**sbox_size):
        count = 0
        if bin(j) == bin(k):
            count += 1
         
        



rows = []
for j in range a:
    rows.append

print(headerlist)