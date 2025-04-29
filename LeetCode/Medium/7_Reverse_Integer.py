import datetime

first_time = datetime.datetime.now()
def rever(x):
    sign = -1 if x < 0 else 1
    x = abs(x)

    rev = int(''.join(reversed(str(x)))) * sign

    if rev < -2147483648 or rev > 2147483647:  # To'g'ri chegarani ishlatish
        return 0
    else:
        return rev
second_time = datetime.datetime.now()

print(rever(1224148798), second_time - first_time)


