list = [...]

def f(list):
    newList = [] # Сюда будут записываться НЕЧЕТНЫЕ числа из переданного списка list
    count = 0    # Сюда будет записываться число НЕЧЕТНЫЕ
    for i in list:  # перебираем list, что бы в i получить каждую циферку 
        if i%2!=0:  # Выбираем только НЕЧЕТНЫЕ
            count += 1 # добавляем единицу в счетчик count
            newList.append(i) # добавляем число i в новый список newList

    summa = sum(newList) 
    return count, summa, min(newList), max(newList), summa/count

# что бы получить "count, summa, min(newList), max(newList), summa/count"
# надо обратиться к функции f, передать туда массив list => f(list)
# и чтобы получить конкретное значение в [] пишешь индекс 
# пример: 
# f(list)[0] >>> count
# f(list)[1] >>> summa
# f(list)[2] >>>  min(newList)

print(f(list)[0])