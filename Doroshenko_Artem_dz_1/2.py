list_cube = []
list_seven = []

# Список кубов нечётных чисел
for i in range(1, 1001):
    if (i % 2 == 1):
        list_cube += [i ** 3]

# Список чисел, которые нацело делятся на 7
for i in range(len(list_cube)):
    num = list_cube[i]
    list_num = [int(a) for a in str(num)]
    sum_num = 0
    for j in range(len(list_num)):
        sum_num += list_num[j]
    if (sum_num % 7 == 0):
        list_seven += [num]

sum_list_seven = sum(list_seven)
print(sum_list_seven)

# Список кубов чисел, увеличенных на 17
for i in range(len(list_cube)):
    list_cube[i] = list_cube[i] + 17

# Список кубов чисел, увеличенных на 17, которые делятся нацело на 7 (*)
list_lenght = len(list_cube)
last_item = list_cube[list_lenght - 1]
control_num = 0
index = 0
while control_num != -1:
    control_num = list_cube[index]
    if (control_num == last_item):
        control_num = -1
    else:
        num = list_cube[index]
        list_num = [int(a) for a in str(num)]
        sum_num = 0
        for i in range(len(list_num)):
            sum_num += list_num[i]
        if (sum_num % 7 != 0):
            list_cube.pop(index)
            index -= 1
        index += 1

sum_new_list_seven = sum(list_cube)
print(sum_new_list_seven)
