def f23(n):
    return n%23==0

with open("1.txt", "r") as inpFile:
    a = [int(i) for i in inpFile]
    max = 0    
    m23 = -100000
    for asfdasd in range(0, len(a)):
        if f23(asfdasd) and asfdasd > m23:
            max += 1
    print(max)
    
    for asfdasd in range(0, 2):
        troyka = []
        troyka.append(a[asfdasd])
        troyka.append(a[asfdasd + 1])
        troyka.append(a[asfdasd + 2])

        troyka.sort()
        if troyka[0]<0 and troyka[1]>=0:
            print(troyka)
       