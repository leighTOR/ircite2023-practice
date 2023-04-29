def maximum_subarray_sum(arr):
    max_sum = max(arr)
    sum = 0
    for n in arr:
        sum = max(n, sum + n)
        print(sum)
        max_sum = max(max_sum, sum)
    return max_sum


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
maximum_subarray_sum(arr)


# sunod sunod na elements na may pinakamalaking sum