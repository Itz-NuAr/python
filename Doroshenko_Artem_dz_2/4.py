data = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for i in range(len(data)):
    info = data[i]
    list_info = info.split()
    name = list_info[-1].capitalize()
    print(f'Привет, {name}!')
