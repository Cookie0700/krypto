import random
import csv

count = 10000
list32 = list(range(32))

    
for i in range(count): 
    filename = str(i)+".csv"
    f = open("./SBox/Random_SBox/"+filename, "w")
    random.shuffle(list32)
    for i in range(32):
        f.write(str(i)+","+str(list32[i])+"\n")
    