done = ''
mark = 0
countMark = 0
with open("fastZadanie/data.txt", "r", encoding="utf-8") as data:
    for fi in sorted(data):
        fulll = fi.split()
        mark += int(fulll[2])
        countMark += 1
        done += f"{fulll[0]} {fulll[1][0]}\n"

with open("fastZadanie/output.txt", "w", encoding="utf-8") as output:
    output.write(done)
    output.write(str(mark/countMark))
