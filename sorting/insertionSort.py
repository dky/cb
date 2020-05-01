def insertionSort(arr):

    for i in range(len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break


if __name__ == "__main__":
    # Best case
    # O(n) - runtime - (why would you pass a sorted array into a sorting algo?)
    # O(1) - space
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # worse case - in this case every element needs to get sorted.
    # O(n^2) - runtime
    arr2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    insertionSort(arr2)
    print(arr2)
