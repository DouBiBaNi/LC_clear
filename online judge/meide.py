import sys


## 1

def quickSort(lst, left=0, right=None) -> None:
    if right is None:
        right = len(lst) - 1

    def _partition(lst, left, right):
        tmp = lst[left]
        while left < right:
            while lst[right] >= tmp and left < right:  # put (< tmp) on the blank
                right -= 1
            lst[left] = lst[right]
            while lst[left] <= tmp and left < right:
                left += 1
            lst[right] = lst[left]
        lst[left] = tmp
        return left

    if left < right:
        mid = _partition(lst, left, right)
        quickSort(lst, left, mid - 1)
        quickSort(lst, mid + 1, right)


for line in sys.stdin:
    nums = list(map(int, line.split()))
    quickSort(nums)
    print(nums)


## 2.
path = []
path.copy()