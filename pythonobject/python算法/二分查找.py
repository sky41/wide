numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 18, 24, 30, 43, 56]
head, tail = 0, len(numbers)
search = int(input("enter"))

while tail - head > 1:
    mid = (head+tail) // 2
    if search < numbers[mid]:
        tail = mid
    if search > numbers[mid]:
        start = mid + 1
    if search == numbers[mid]:
        ans = mid
        break
else:
    if search == numbers[head]:
        ans = head
    else:
        ans = -1
print(ans)
