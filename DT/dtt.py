from collections import Counter

lst = [1, 2, 3, 2, 4, 5, 1, 6, 3]

duplicates = [item for item, count in Counter(lst).items() if count > 1]

print(duplicates)
