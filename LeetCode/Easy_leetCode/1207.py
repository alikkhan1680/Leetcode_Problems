from scipy.stats import false_discovery_control


def uniqueOccurrences(nums):

    dic = {}
    for i in nums:
        key = str(i)
        if key in dic:
            dic[key] +=1
        else:
            dic[key] = 1
    values = list(dic.values())
    unique = set(values)


    if len(values) == len(unique):
        return True
    else:
        return False






print(uniqueOccurrences([1,2,2,1,1,3]))