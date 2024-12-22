data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
to_list = [1, 3, 7, 8, 9, 10, 15, 13, 19, 20, 33, 15, 21, 45, 77, 89, 34, 56, 78, 90, 11, 22, 33, 44, 55, 66, 77, 88, 99, 111, 222, 333, 1 ,15, 24,]
print(len(data), len(to_list))
new_list = []
sublist = []
e = 0

for i in range(1, len(data)):
    if data[i] == data[i - 1] and e < 9:
        e += 1
        sublist.append(data[i - 1])
    else:
        sublist.append(data[i - 1])
        new_list.append(sublist)
        sublist = []
        e = 0

if sublist:
    sublist.append(data[-1])
    new_list.append(sublist)

print(new_list)

result = []
index = 0
for sublist in new_list:
    count = len(sublist)
    result.append(to_list[index:index + count])
    index += count

print(result)
