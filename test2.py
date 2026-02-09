def asd(*countPrice):
    if len(countPrice)%2!=0:
        return "Ошибка"

    bank = 0
    for i in range(0, len(countPrice), 2):
        bank += countPrice[i] * countPrice[i+1]
    return bank

print(asd(2,2,6,4,5,5))
# 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

# git config --global user.email "frumasg@gmail.com"
# git config --global user.name "SLoKI1"