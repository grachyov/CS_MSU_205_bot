def s1(x):
    if 11 <= x % 100 <= 19 or 5 <= x % 10 <= 9 or x % 10 == 0:
        return "ов"
    elif 2 <= x % 10 <= 4:
        return "а"
    else:
        return ""

def s2(x):
    if 11 <= x % 100 <= 19 or 5 <= x % 10 <= 9 or x % 10 == 0:
        return ""
    elif 2 <= x % 10 <= 4:
        return "ы"
    else:
        return "у"
