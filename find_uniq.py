def find_uniq(arr):
    if arr[0] == arr[1]:
        for i in arr:
            if i != arr[0]:
                return i
    elif arr[0] == arr[2]:
        return arr[1]
    else:
        return arr[0]