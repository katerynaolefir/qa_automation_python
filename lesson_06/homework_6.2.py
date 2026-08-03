while True:
    enter_word = input('Введіть слово: ').lower()
    if 'h' in enter_word:
        print('Слово з літерою "h" введено')
        break
    else:
        print('Слово введено без літери "h"')