num = int(input("Enter nth term: "))
i = 0

#only iterate for as many terms as you want
while i < num:
    #first term is always 1
    if i == 0:
        series = [1]
    else:
        cnt = 1
        tmpseries = []
        #iterate for each term in series if bigger than 1 to check the digit preceeding the current digit
        for j in range(1, len(series)):
            #if digits are equal, increment the number that will come FIRST in the resulting series of this iteration
            #always looking at the current digit and the previous digit to see what will come next
            if series[j] == series[j - 1]:
                cnt += 1
            #if the current digit ISNT equal to the previous digit, we KNOW there is only 1 of the PREVIOUS digit because it changed from previous to current
            else:
                #so start the new series with the count of how many times the previous digit appeared followed by THAT previous digit
                # IE - 21 goes to "12" + rest of the series
                tmpseries += [cnt, series[j - 1]]
                #cnt is just the number of times you see the current number! this is why it is always added at the start of the tmpseries
                cnt = 1
        tmpseries += [cnt, series[len(series) - 1]]
        series = tmpseries
    i += 1
    print("Term", i, "-", series)
