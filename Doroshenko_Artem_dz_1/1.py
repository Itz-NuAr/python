s = int(input('duration = '))
if (s < 0):
    print('error, duration < 0')
elif (s < 60):
    print(str(s) + ' сек')
elif (s < 3600):
    m = s // 60
    s %= 60
    print(str(m) + ' мин ' + str(s) + ' сек')
elif (s < (3600 * 24)):
    m = s // 60
    s %= 60
    h = m // 60
    m %= 60
    print(str(h) + ' час ' + str(m) + ' мин ' + str(s) + ' сек')
else:
    m = s // 60
    s %= 60
    h = m // 60
    m %= 60
    d = h // 24
    h %= 24
    print(str(d) + ' дн ' + str(h) + ' час ' + str(m) + ' мин ' + str(s) + ' сек')
