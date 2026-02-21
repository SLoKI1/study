res = []
restext = ""

for fileReadEl in open("ClassWork/les1/fruit.txt", mode='r', encoding='utf-8'):
    fruktFile = fileReadEl.split()
    for frukt in fruktFile:
        if not frukt in res:
            res.append(frukt)
            restext += f"{frukt} - {fruktFile.count(frukt)}\n"
    print(restext)
    print(" ".join(res))
    print(" ".join(sorted(fruktFile)))