def narcissistic( value ):
    snum = str(value)
    digit = len(snum)
    summa = 0
    print(snum, digit)
    for i in range(digit):
        num = (int(snum[i]))**digit
        print(num)
        summa += num
    if value == num:
        return True
    else:
        return False
narcissistic(371)

