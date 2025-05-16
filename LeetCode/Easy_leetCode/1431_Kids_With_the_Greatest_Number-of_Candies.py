def Candies(candies, extra_candies):
    max_condies = max(candies)
    resualt = []
    print(resualt)
    for i in range(len(candies)):
        if candies[i] + extra_candies >= max_condies:
            resualt.append(True)
        else:
            resualt.append(False)

    return resualt

print(Candies([5, 8, 2, 10, 6], 3))