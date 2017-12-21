"""
Задание 1
Пишем функцию, которая выводит второе по возрастанию значение из
переданных аргументов. Учитываем, что может быть повторяющиеся значения аргументов.

"""
def sec_max(my_string):
    for i in range(0, len(my_string)):
        try:
            float(my_string[i])
            i = int(i)
        except ValueError:
            print("Ошибка в списке есть не число")
            break
    my_string = list(my_string)
    my_string.sort()
    for i in range(0,my_string.count(my_string[0])):
        my_string.remove(my_string[0])
    return my_string[0]

x = [3,0,2,5,3,1,1,1,25]

print(sec_max(x))




