from mtgsdk import Card

def mergeSortAlg(cardList):
    #if there's only one elememt
    if len(cardList) == 1:
        return cardList
    midpoint = len(cardList) // 2
    left = cardList[:midpoint]
    leftArr = mergeSortAlg(left)
    right = cardList[midpoint:]
    rightArr = mergeSortAlg(right)
    result = mergeArr(leftArr, rightArr)
    return result

def mergeArr(leftarr, rightarr):
    merged = []
    leftPointer = 0
    rightPointer = 0
    #increment pointers until all elements are visited
    while leftPointer < len(leftarr) and rightPointer < len(rightarr):
        #add to the resulting array from least to greatest 
        if leftarr[leftPointer] < rightarr[rightPointer]:
            merged.append(leftarr[leftPointer])
            leftPointer = leftPointer + 1
        elif leftarr[leftPointer] >= rightarr[rightPointer]:
            merged.append(rightarr[rightPointer])
            rightPointer = rightPointer + 1

    #if one array is not done then add the remaining
    if leftPointer == len(leftarr):
        merged.extend(rightarr[rightPointer:])
    if rightPointer == len(rightarr):
        merged.extend(leftarr[leftPointer:])    
       
    return merged        