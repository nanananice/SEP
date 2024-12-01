def binary_search(find,numlist):
    mid = len(numlist)//2
    if (find not in numlist): 
        return False
    if (numlist[mid] == find):
        return mid
    elif (numlist[mid] < find):
        return binary_search(find,numlist[mid:])+ mid
    elif (numlist[mid] > find):
        return binary_search(find,numlist[:mid])
    

print(binary_search(-1,[2,3,4,7,8]))