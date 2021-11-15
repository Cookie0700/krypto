import csv
#from prettytable import PrettyTable

#def out_ddt(ddt: list):
    #with open('ddt', mode='w') as ddt_file:
     #  ddt_write = csv.writer(ddt_file,delimiter=',',quoting=csv.QUOTE_MINIMAL)

def csv_print(ddt: list):
    f = open('ddt.csv', 'w', newline='')
    writer = csv.writer(f, delimiter=';', quotechar='|')
    for i in range(1,32):
        row = []
        for j in range(1,32):
            row.append(len(ddt[i][j]))
        print(row)
        writer.writerow(row)
    f.close()

#def test2(ddt: list):

"""
def test2(ddt: list):
    r = []
    for x in range(31):
        r.append(x) 
    t = PrettyTable()
    t.field_names = r
    t.align='l'
    t.border=False
    f = open('ddt2.csv', 'w', newline='')
    writer = csv.writer(f, delimiter=' ', quotechar='|')
    for i in range(1,32):
        row = []
        for j in range(1,32):
#            string = ddt[i][j][0]
            row.append((ddt[i][j])[:2:2])
        t.add_row(row)
        print(row)
        writer.writerow(row)
    f.close()
    print(t)
"""