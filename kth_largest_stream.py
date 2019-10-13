def kthLargest(a,n,k):

    # code here
    arr = [0]*k
    for i in range(k):
        arr[i] = a[i]
        a[i] = -1
    build_heap(arr, k)
    a[i] = arr[0]
    for i in range(k, n):

        if arr[0] < a[i]:
            arr[0] = a[i]
            heapify(arr, k, 0)

        a[i] = arr[0]

    for i in a:
        print(i, end = " ")

def build_heap(arr, n):
    for i in range((n-1)//2, -1, -1):
        heapify(arr, n, i)



def heapify(arr, n, i):
    l = i*2 + 1
    r = i*2 + 2

    if l < n and arr[l] < arr[i]:
        smallest = l
    else:
        smallest = i

    if r < n and arr[r] < arr[smallest]:
        smallest = r

    if smallest is not i:
        arr[smallest], arr[i] = arr[i], arr[smallest]
        heapify(arr, n, smallest)

arr = [857 ,744, 492, 228, 366, 860, 937, 433, 552, 438, 229, 276, 408, 475, 122]
n = 15
k = 3

kthLargest(arr, n, k)
