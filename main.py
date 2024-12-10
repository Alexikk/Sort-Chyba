import random

# 1, Bubble sort
array = [22, 66, 94, 69, 1, 99, 6, 14, 88, 3]

def bubble_sort():
    n = len(array)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
            print(array) 
    return array

print("Bubble sort:", bubble_sort())

# 2, Bogo sort
arrayb = [86, 62, 6, 79, 21, 14, 2, 70, 37, 28]

def is_sorted(arrayb):
    for i in range(1, len(arrayb)):
        if arrayb[i] < arrayb[i-1]:
            return False
    return True

def bogosort(arrayb):
    count = 0
    while not is_sorted(arrayb):
        random.shuffle(arrayb)
        count += 1
        print(f"Pokus {count}: {arrayb}")
    print(f"Seznam seřazen po {count} pokusech.")
    return arrayb

print("Bogo sort:", bogosort(arrayb))


# 3, Selection sort
arrays = [58, 31, 23, 9, 18, 13, 67, 89, 5, 72]

def selection_sort(arrays):
    n = len(arrays)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arrays[j] < arrays[min_index]:
                min_index = j
        arrays[i], arrays[min_index] = arrays[min_index], arrays[i]
        print(f"Krok {i + 1}: {arrays}")
    return arrays

print("Selection sort:", selection_sort(arrays))


# 4, Insertion sort
arrayi = [47, 24, 17, 45, 19, 13, 29, 58, 6, 32]

def insertion_sort(arrayi):
    for i in range(1, len(arrayi)):
        key = arrayi[i]
        j = i - 1
        while j >= 0 and key < arrayi[j]:
            arrayi[j + 1] = arrayi[j]
            j -= 1
        arrayi[j + 1] = key
        print(f"Krok {i}: {arrayi}")
    return arrayi

print("Insertion sort:", insertion_sort(arrayi))



