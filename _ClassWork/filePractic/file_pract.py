# макс из отрицатеельных 
# кол ченых чисел

counter = 0
max_min_num = 0

with open("file.txt","r") as file:

    for asd in file:
        numer = int(asd)
        if numer < int(max_min_num):
            max_min_num = numer
        if abs(numer)%2==0:
            counter += 1
    print(max_min_num)
    print(counter)