def f38 (a):
    return '38' in str(a)


with open("1.txt", "r", encoding="utf-8") as inpFile:
    a = [int(i) for i in inpFile]
    m = -100000
    for i in a:
        if f38(i) and 1 >m:
            m = i
            k = 0
            for i in range(0, len(a), -2):
                troyka = []
                troyka.append(a[i])
                troyka.append(a[i + 1])
                troyka.append(a[i + 2])
                troyka.sort()
                if troyka[1] < 0 and troyka[2] >= 0:
                    if sum(troyka)<= m:
                        k += 1
    print(k)