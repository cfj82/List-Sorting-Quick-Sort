#  Quick Sort

def partition(data_set, low, high):
    i = (low-1)  # pointer for greater element, set at left end
    pivot = data_set[high]  # set pivot spot to right most

    for j in range(low, high):  # go through all elements
        if data_set[j] <= pivot:  # compare all numbers to pivot
            i = i + 1  # move greater element to right by 1
            (data_set[i], data_set[j]) = (data_set[j], data_set[i])  # rotate position j with position i for low

    # swap pivot with the greater element specified by i
    (data_set[i + 1], data_set[high]) = (data_set[high], data_set[i + 1])

    return i + 1  # return set ordered with pivot in middle


def quicksort(data_set, low, high):
    if low < high:  # if low < high then continue
        pivot = partition(data_set, low, high)  # run partition to set new pivot

        quicksort(data_set, low, pivot-1)  # run quicksort left of pivot. order is low to pivot

        quicksort(data_set, pivot+1, high)  # run quicksort right of pivot. order is pivot to high


data_set = [2, 3, 5, 4, 8, 2, 9]
print('Unorganized data set is: ' + str(data_set))

size = len(data_set)

quicksort(data_set, 0, size-1)

print('\n The data in sorted order is: ')
print(data_set)
