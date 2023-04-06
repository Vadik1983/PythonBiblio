txt = (input("Введите текст заглавными буквами: "))

def scrabble(word): # Код не работает
    count = 0
        
    for i in txt:
        if (i == 'A') or (i == 'E')  or (i == 'I') or (i == 'O') or (i ==  'U') or (i == 'L') or (i == 'N')  or (i == 'S') or (i == 'T') or (i ==  'R'):
            count = count + 1
        elif (i == 'D') or (i == 'G'):
            count = count + 2
        elif (i == 'B') or (i == 'C')  or (i == 'M') or (i == 'P'):
            count = count + 3
        elif (i == 'F') or (i == 'H')  or (i == 'V') or (i == 'W') or (i ==  'Y'):
            count = count + 4
        elif (i == 'k'):
            count = count + 5
        elif (i == 'J') or (i == 'X'):
            count = count + 8
        elif (i == 'Q') or (i == 'Z'):
            count = count + 10
    print(count)

scrabble(txt)
