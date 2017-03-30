"""
sort the number list from min to max
"""


def number_sort(numbers):
    len1 = len(numbers)
    for i in range(len1):
        for j in range(len1-i):
            if j+1 < len1:
                if numbers[j] > numbers[j+1]:
                    (numbers[j], numbers[j+1])=(numbers[j+1], numbers[j])
    return numbers