a = [78, 67, 44, -100, 87, 321, 0]
print(a)

# for index, value in enumerate(a):
#     if value % 2 == 0:
#         a[index] = a[index] + 1
#     else:
#         a[index] = a[index] - 1
# print(a)

for index in range(0, len(a)):
    if index % 2 == 0:
        a[index] = a[index] + 1
    else:
        a[index] = a[index] - 1

print(a)

# a[0] = 100
# a[-1] = 100
# print(a)
