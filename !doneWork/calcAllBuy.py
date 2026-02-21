
# задача посчитать сколько заплатим за все это количество*цена+количество*цена+...
# формат количество, цена, количество, цена ...
# Ввод: 2,2,6,4,5,5

def asd(*countPrice):
    if len(countPrice)%2!=0:
        return "Ошибка"

    bank = 0
    for i in range(0, len(countPrice), 2):
        bank += countPrice[i] * countPrice[i+1]
    return bank

print(asd(2,2,6,4,5,5))