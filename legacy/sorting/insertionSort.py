def insertionSort(arr):
    # arr length is 10.
    # for i in range, 1 -> 10
    # start at index 1.
    for i in range(1, len(arr)):
        # 1, 2, 3, 4, 5, 6, 7, 8, 9 vs 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
        print("outer", i)
        for j in range(i, 0, -1):
            print(j)
            print(arr[j], arr[j-1])
            # if arr[j] < arr[j-1]:
                # arr[j], arr[j-1] = arr[j-1], arr[j]
            # else:
                # break
                    


if __name__ == "__main__":
    # best case
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # worse case
    arr2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    insertionSort(arr1)
    # print(arr2)
