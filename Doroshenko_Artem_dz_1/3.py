for i in range(1, 101):
    N = i
    list_N = [int(a) for a in str(N)]
    if (list_N[-1] == 1 and N != 11):
        print(str(N) + ' процент')
    elif (list_N[-1] == 2 or list_N[-1] == 3 or list_N[-1] == 4):
        if (N != 12 and N != 13 and N != 14):
            print(str(N) + ' процента')
        else:
            print(str(N) + ' процентов')
    else:
        print(str(N) + ' процентов')
