num = int(input("Enter nth term: "))
i = 0

while i < num:
    if i == 0:
        series = [1]
    else:
        cnt = 1
        tmpseries = []
        for j in range(1, len(series)):
            if series[j] == series[j - 1]:
                cnt += 1
            else:
                tmpseries += [cnt, series[j - 1]]
                cnt = 1
        tmpseries += [cnt, series[len(series) - 1]]
        series = tmpseries
    i += 1
    print("Term", i, "-", series)
