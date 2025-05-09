def mergeAlternately(word1, word2):
    merge = []
    for i in range(max(len(word1), len(word2))):
        if i < len(word1):
            merge.append(word1[i])
        if i < len(word2):
            merge.append(word2[i])
    result = ''.join(merge)
    return result



print(mergeAlternately('asd', 'zxc'))