def iniciali(inputFile, outputFile):
    with open(inputFile, "r", encoding="utf-8") as contentInput:
        all = ""
        for content in contentInput:
            line = content.split()
            all += f"{line[0]} {line[1][0]}. {line[2][0]}. \n"
        with open(outputFile, "w", encoding="utf-8") as contentOutput:
            contentOutput.write(all)

def mony(inputFile, outputFile):
    with open(inputFile, "r", encoding="utf-8") as contentInput:
        counterrMember = 0
        sumStage = 0
        bank = 0
        for content in contentInput:
            line = content.split()
            counterrMember += 1
            sumStage += int(line[3])
            zp = float(line[4])
            ndfl = zp * 0.1
            resZp = round(zp - ndfl,2)
            bank += resZp
        with open(outputFile, "w", encoding="utf-8") as contentOutput:
            contentOutput.write(f"Cредний стаж: {round(sumStage/counterrMember,2)}\n")
            contentOutput.write(f"Банк ЗП: {bank}")


iniciali("data.txt","spisok.txt")
mony("data.txt","finrez.txt")