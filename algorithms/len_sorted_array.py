def len_sorted_array(array):
    if not array:
        return 0
    i = 0
    for j in range(1, len(array)):
        if array[j] != array[i]:
            i += 1
            array[i] = array[j]
    return i + 1