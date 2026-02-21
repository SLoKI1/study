fruktArr = []
res = []
restext = ""

while True:
    frukt = input("Введите фпукты. Выход - 0.: ").lower()
    if frukt == "0":
        for frukt in fruktArr:
            if not frukt in res:
                res.append(frukt)
                restext += f"{frukt} - {fruktArr.count(frukt)}\n"
        print(restext)
        print(" ".join(res))
        print(" ".join(sorted(fruktArr)))
        break
    fruktArr.append(frukt)
