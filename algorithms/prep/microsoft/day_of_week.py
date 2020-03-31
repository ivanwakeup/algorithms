'''
given a day of the week from ("Mon", "tue", "wed", "thu", "fri", "sat", "sun") and an integer K,
return a day of the week that is K days later than the given day

examples:
"mon", 2 => "wed"
"sat", 23 => "mon"


solution:
represent days of week in array, return array[K%7]
'''


def day_of_week(day, k):
    days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    day_idx = days.index(day)
    return days[(k+day_idx)%7]

print(
    day_of_week("sat", 23)
)