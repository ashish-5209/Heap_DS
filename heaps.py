def max_heap(arr, i):
    l = 2*i + 1
    r = 2*i + 2

    if l < len(arr) and arr[l] > arr[i]:
        largest = l
    else:
        largest = i

    if r < len(arr) and arr[r] > arr[largest]:
        largest = r

    if largest is not i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heap(arr, largest)

def build_heap(arr):
    for i in range(len(arr)//2-1, -1, -1):
        max_heap(arr, i)

def extract_max(arr):
    if len(arr) < 0:
        return "Heap UnderFlow"

    max = arr[0]
    arr[0] = arr[len(arr) - 1]
    arr.pop()
    max_heap(arr, 0)
    return max


def increase_key(arr, i, key):
    if key < arr[i]:
        return "Error"
    arr[i] = key

    while i > 0 and arr[(i-1) // 2] < arr[i]:
        arr[i], arr[(i-1)//2] = arr[(i-1)//2], arr[i]
        i = (i-1)//2

def heap_sort(arr):
    lis = []
    for i in range(len(arr)-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        lis.insert(0,arr[i])
        arr.pop()
        max_heap(arr, 0)
    lis.insert(0,arr[0])
    return lis

arr = [18, 3, 56, 89, 32, 8, 9, 11, 76]
build_heap(arr)

print("Array after Build Heap.")
for i in arr:
    print(i, end=" ")

print()

print("Array after Increase Key.")
increase_key(arr, 8, 100)
for i in arr:
    print(i, end=" ")
print()

print("Array after extract maximum.")
print(extract_max(arr))
for i in arr:
    print(i, end=" ")
print()

print("Array after heap sort")
print(heap_sort(arr))

