def count_pairs(arr, k):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    count = 0
    for num, freq_num in freq.items():
        if num - k in freq:
            count += freq[num - k] * freq_num
    return count


arr = [1, 7, 5, 9, 2, 12, 3]
k = 2
print(count_pairs(arr, k))














"""
def counting_pairs(arr, k):
    # sort the array
    arr.sort()
    # pair numbers with difference of two




arr = [1, 7, 5, 9, 2, 12, 3]
k = 2
counting_pairs(arr, k)
"""