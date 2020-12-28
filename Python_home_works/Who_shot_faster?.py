# Два участника p1 и p2 участвуют в дуэли.
# Напишите функцию whos_first, которая принемает две строки 
# и возвращает имя игрока, который выстрелил первым.
# Если игроки выстрелили одновременно, то вернуть строку "tie".
# Примечание:
# передаваемые строки - могут быть различной длины!
# (то есть содержать различное количество пробелов)

p1 = "     Bang!"
p2 = "    Bang! "

def whos_first(p1, p2):
    '''
    DOCSRING: the function calculates who was the first,
              by finding the desired character in the string
    INPUT:    the input is given two arguments that contain strings
    OUTPUT:   the output returns the name of the one who was the first
    '''
    if p1.find("B") < p2.find("B"):
        return "p1"
    elif p1.find("B") > p2.find("B"):
        return "p2"
    else:
        return "tie"

