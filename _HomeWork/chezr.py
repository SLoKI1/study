try:
    word = input("Введите слово:")
    rightNum = int(input("Введите число сдвига:"))

    alfafit = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    codeWord = ""
    for char in word.lower():
        if char in alfafit:
            indexChar = alfafit.find(char)
            newChar = indexChar + rightNum
            if newChar >= 33:
                newChar -= 33
            codeWord += alfafit[newChar]
        else:
            print(f'{word} не содержится в русском алвавите')

    print(codeWord)
except IndexError:
    print("Вы ввели не число")
except:
    pass