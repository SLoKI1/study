# def asd(*countPrice):
#     if len(countPrice)%2!=0:
#         return "Ошибка"

#     bank = 0
#     for i in range(0, len(countPrice), 2):
#         bank += countPrice[i] * countPrice[i+1]
#     return bank

# print(asd(2,2,6,4,5,5))


def sisc(a,b,c):
    d = b*b-4*a*c
    if d >= 0:
        x1 = (-b - d**0.5)/(a*2)
        x2 = (-b + d**0.5)/(a*2)
    elif d == 1: