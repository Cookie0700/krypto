import csv

#def out_ddt(ddt: list):
    #with open('ddt', mode='w') as ddt_file:
     #  ddt_write = csv.writer(ddt_file,delimiter=',',quoting=csv.QUOTE_MINIMAL)

def test(ddt: list):
    f = open('ddt.csv', 'w', newline='')
    writer = csv.writer(f, delimiter=' ', quotechar='|')
    for i in range(1,32):
        row = []
        for j in range(1,32):
            row.append(len(ddt[i][j]))
        print(row)
        writer.writerow(row)
    f.close()