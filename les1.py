import random

a = []
for i in range(10):
    a.append(random.randint(1,125))

# a = [103, 26, 59, 96, 17, 118, 26, 28, 59, 42]

def detect_nechotnoe(arr):
    newArr = []
    a = 0 
    b = 0
    for i in arr:
        if i%2!=0:
            b += i
            a += 1
            newArr.append(i)
    minarr = min(newArr)
    maxarr = max(newArr)
    avg = sum(newArr)/len(newArr)
    
    return f"""
{arr=}
{newArr=}
-----------------
Нечетных: {a}
Сумма: {b}
Минимальное: {minarr}
Максимальное: {maxarr}
Среднее: {round(avg,2)}
-----------------
Индекс максимального: Индекс: {detect_index_num(newArr)[0]} - число: {detect_index_num(newArr)[1]}"""


def detect_index_num(arr):
    indexStorage = 0 
    numStorage = 0
    for index, num in enumerate(arr):
        if num>numStorage:
            indexStorage = index
            numStorage = num

    return indexStorage, numStorage



print(detect_nechotnoe(a))