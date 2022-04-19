from mtgsdk import Card

def quickSortAlg(cardList, down, up):
    #if there's only one elememt
    if len(cardList) > 1:
        if down < up:
            pivot = quickdown(cardList, down, up)
            quickSortAlg(cardList,down, pivot-1)
            quickSortAlg(cardList,pivot+1, up)

def quickdown(subArr,low,high):
    pivot = subArr[low]
    up = low
    down = high
    while(up < down):
        for i in range(up, high):
            if subArr[up] > pivot:
                break
            up = up + 1
        for j in reversed(range(low, high)):
            if subArr[down] < pivot:
                break
            down = down - 1            
        if(up < down):
            temp = subArr[up]
            subArr[up] = subArr[down]
            subArr[down] = temp
    temp = subArr[low]    
    subArr[low] = subArr[down]
    subArr[down] = temp
    return down   
