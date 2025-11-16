arr = list(map(int, input().split()))
k = int(input())

def rotate(arr, k):
    n = len(arr)
    k %= n
    if k < 0:
        k += n

    def rev(i, j):
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    rev(0, n-1)
    rev(0, k-1)
    rev(k, n-1)

rotate(arr, k)
print(*arr)
