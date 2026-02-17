arr = [2, 0, 1, 2, 0, 1]

count0 = count1 = count2 = 0
i = 0

while i < len(arr):
    if arr[i] == 0:
        count0 += 1
    elif arr[i] == 1:
        count1 += 1
    else:
        count2 += 1
    i += 1

arr = [0]*count0 + [1]*count1 + [2]*count2
print(arr)
