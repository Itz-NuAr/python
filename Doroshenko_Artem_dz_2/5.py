items = [5.64, 50.44, 162.23, 35.79, 93, 171.46, 127.5, 197.15, 62.48, 98.77, 11.77, 165.91, 164.36, 61.86]
# A
print('A')
string_a = ''
for i in range(len(items)):
    item = str(items[i])
    spl_item = item.split('.')
    if len(spl_item) > 1:
        r = int(spl_item[0])
        kk = spl_item[1]
        if len(kk) == 1:
            kk = f'0{kk}'
            fixed_item = f'{r}.{kk}'
            items[i] = float(fixed_item)
        result = f'{r} руб {kk} коп'
    else:
        r = int(item)
        result = f'{r} руб 00 коп'
    string_a += f'{result}, '
print(string_a)
# B
print('\nB')
first_id = id(items)
items.sort()
second_id = id(items)
print(items)
print(f'id before sort = {first_id}, id after sort = {second_id}')
# C
print('\nC')
new_items = items
new_items.reverse()
print(new_items)
# D
print('\nD')
print(f'{new_items[:5]}')  # минимум кода =D
