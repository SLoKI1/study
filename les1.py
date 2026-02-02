# import random
# a = []
# for i in range(10):
#     a.append(random.randint(1,125))


a = [123, 26, 59, 96, 17, 118, 26, 28, 59, 42]

def detect_nechotnoe(arr):
    a = 0 
    b = 0
    for i in arr:
        if i%2!=0:
            b += i
            a += 1
    minarr = min(arr)
    maxarr = max(arr)
    return f"Нечетных: {a}\nСумма: {b}\nМинимальное: {minarr}\nМаксимальное: {maxarr}"

print(detect_nechotnoe(a))