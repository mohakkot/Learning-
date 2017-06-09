def insertionSort(ar):
    shift = 0
    for i in range(1, len(ar)):
        for j in range(i-1, -1, -1):
            k,m = 0, 0
            if ar[j+1] < ar[j]:
                k =i; m = j
                ar[j+1], ar[j] = ar[j], ar[j+1]
                print(ar)
            shift = shift + k - m
            print(shift)
    return shift

s = int(input())
ar = [int(B) for B in input().strip().split(' ')]
shift =insertionSort(ar)
print(shift)
