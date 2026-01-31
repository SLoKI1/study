inputInt = int(input("Введите число: "))


# def scontor_chislo(num):
#     if num%2 == 0:
#         return "Четное число"
#     else: 
#         return "Нечетное число"
    
# print(scontor_chislo(inputInt))



# --------------------------------------------------------------------------



# def vozvedenie(num, stepen):
#     return num ** stepen

# print(vozvedenie(inputInt, 2))




# --------------------------------------------------------------------------



# def ploshad(num1, num2):
#     return num1 * num2
# print(ploshad(inputInt, 5))




# --------------------------------------------------------------------------



# def coren(a, b):
#     return b/a 
# print(coren(2,inputInt))  



# --------------------------------------------------------------------------

# ---------------------------- ЗАДАЧА ----------------------------

# --------------------------------------------------------------------------



height_wallpaper = 10
length_wallpaper = 1.6


def options(a,  #Длина 
            b,  #ширина
            c,  #высота
            bd, #ширина двери
            cd, #высота двери
            bo, #ширина окна
            co, #высота окна
            k  #количество окон
            ):
    
    perimetr_comtati = 2 * (a + b)
    ploshad_sten = perimetr_comtati * c
    ploshad_dveri = bd * cd
    ploshad_okon = bo * co * k
    itog_ploshad = ploshad_sten - ploshad_dveri - ploshad_okon
    kolichestvo_oboev = itog_ploshad / (height_wallpaper * length_wallpaper)
    return f"Вам потребуется {round(kolichestvo_oboev)} рулонов обоев"  


# print(options(4, 3, 2.5, 0.8, 2, 1, 1, 1)) 
print(options(5, 4, 3, 1, 2, 1.5, 1.5, 2))    