def findMaxAverage(nums, k):

    index = 0
    val = []
    for i in range(len(nums)):
        avaerg = sum(nums[index : index+4]) / 4
        index +=1
        val.append(avaerg)
    return max(val)





print(findMaxAverage([1,12,-5,-6,50,3], 4))
