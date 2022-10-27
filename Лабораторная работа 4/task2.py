#функция, возвр. словарь с количеством букв
def get_count_char(str_):
    strcopy = ''.join(list(main_str.lower().split()))  # склеенный список всех слов
    strmn =[] # список букв без повтора
    for b in strcopy:
        if b not in strmn and b.isalpha():
            strmn.append(b)
    d = dict() #словарь
    for c in strmn:
        d[c] = strcopy.count(c)
    return d
#функция возвр. словарь с процентным соотношением
def procent(slovar):
    f = dict()
    for letter in slovar.keys():
        f[letter] = str(round(int(slovar.get(letter))/int(sum(slovar.values()))*100, 2)) + '%'
    return f

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
print(procent(get_count_char(main_str)))

