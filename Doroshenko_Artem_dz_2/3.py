data = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
last_item = data[len(data) - 1]
cur_item = ''
index = 0
first_id = id(data)
while cur_item != last_item:
    cur_item = data[index]
    try:
        num = abs(int(data[index]))
        prev_num = data[index]
        if num < 10:
            num = (f'{num:02d}')
        if '+' in prev_num:
            num = f'+{num}'
        if '-' in prev_num:
            num = f'-{num}'
        data[index] = str(num)
        data.insert(index, '"')
        data.insert(index + 2, '"')
        index += 2
    except ValueError:
        index += 1

result = ''
i = 0
while i < len(data):
    if data[i] == '"':
        result += f'{data[i]}{data[i + 1]}{data[i + 2]} '
        i += 3
    else:
        result += f'{data[i]} '
        i += 1
second_id = id(data)
print(result)
print(f'id before = {first_id}, id after = {second_id}')
print(f'id did not change => list (in place)')
