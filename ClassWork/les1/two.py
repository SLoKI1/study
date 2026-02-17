

fruktArr = []
res = []
restext = ""



for fileReadEl in open("ClassWork/les1/fruit.txt", mode='r', encoding='utf-8'):
    frukt = fileReadEl.split()
    for fruktEl in frukt:
        if not fruktEl in res:
            res.append(frukt)
            restext += f"{frukt} - {fruktArr.count(frukt)}\n"

    # print(restext)
    # print(" ".join(res))
    # print(" ".join(sorted(fruktArr)))
    # break

print(restext)






