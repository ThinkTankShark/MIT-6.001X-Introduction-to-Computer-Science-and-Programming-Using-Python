def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    # Your code here
    tmp = {}
    result = []
    for value in aDict.values():
        if(value in tmp.keys()): tmp[value] += 1
        else: tmp[value] = 1
    for key in aDict.keys():
        if(tmp[aDict[key]] == 1): result.append(key)
    return sorted(result)
