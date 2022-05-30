rettern = [1, 2, 3, 4, 5, 6]
max = 0
for item in rettern:
    item = int(item)
    if max < item:
        max = item
    else:
        max = max
print(max)
