def quick_sort(sequence):
    print(sequence)
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()
    items_greater = []
    items_lower = []
    for item in sequence:
        
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)
    
print(quick_sort([1,3,6,8,5,4,6,4,5,8,7,4,6,7,2,2,3,4,7,6,5,7,9,8,0,8,7,5,7,8,0,7,2,3,4,6,4,5]))