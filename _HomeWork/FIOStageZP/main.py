counterrMember = 0 
bank = 0
sumStage = 0
otchot = ""
with open("_HomeWork/FIOStageZP/testDataFioStageZP.txt", "r", encoding="utf-8") as testDataFioStageZP:
    for element in testDataFioStageZP:
        line = element.split()
        counterrMember += 1

        sumStage += int(line[3])
        zp = int(line[4])
        ndfl = zp * 0.1
        resZp = zp - ndfl
        bank += resZp
        otchot += f"{line[0]} {line[1][0]}. {line[2][0]}. {zp} {ndfl} {resZp}\n"
    with open("_HomeWork/FIOStageZP/otchotFioStageZP.txt", "w", encoding="utf-8") as otchotFioStageZP:
        otchotFioStageZP.write(otchot)
        otchotFioStageZP.write(f"""
{"="*7}ИТОГ{"="*7}
Сотрудников: {counterrMember}
Cредний стаж: {round(sumStage/counterrMember,2)}
Банк ЗП: {bank}
{"="*18}
""")


