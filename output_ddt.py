import csv
from beautifultable import BeautifulTable
from beautifultable.enums import ALIGN_LEFT, ALIGN_RIGHT

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

def ddt_table_values(ddt: list):
    header = []
    for x in range(31):
        header.append(str(x+1)) 
    ddt_table = BeautifulTable(maxwidth=1337, default_alignment=ALIGN_LEFT, precision=2)
    ddt_table.columns.header = header
    f = open('ddt2.csv', 'w', newline='')
    writer = csv.writer(f, delimiter=' ', quotechar='|')
    for i in range(1,32):
        row = []
        for j in range(1,32):
            # Ignore '[]'
            if str(ddt[i][j]) == '[]':
                row.append('')
            else:
                row.append(str(ddt[i][j][::]).strip("[]"))
        ddt_table.rows.append(row)
        # print(row)
        writer.writerow(row)
    f.close()
    return ddt_table
    