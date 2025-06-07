#
# file = open('24_demo (2).txt').read()
#
# k = 1
# m = 0
# for i in range(0, len(file)):
#     if file[i - 1] != file[i]:
#         k += 1
#     else:
#         m = max(m, k)
#         k = 1
#
# print(m)

# file = open('24_demo.txt').read()
#
# k = 1
# m = 0
# work = False
#
#
# for i in range(0, len(file) - 1):
#     if file[i] == 'X':
#         work = True
#     else:
#         work = False
#
#     if work:
#         k += 1
#     else:
#         m = max(m, k)
#         k = 1
#
# print(m - 1)