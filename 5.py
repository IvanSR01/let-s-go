#
# for n in range(100, 999):
#     str_nums = list(str(n))
#     p1 = int(str_nums[0]) * int(str_nums[1])
#     p2 = int(str_nums[1]) * int(str_nums[2])
#
#     f = min(p1, p2)
#     s = max(p1, p2)
#
#     res = str(f) + str(s)
#
#     if res == '621':
#         print(n)
#
#


# for n in range(1, 10000000000):
#     n2 = bin(n)[2:]
#
#     one_count_2 = bin(n2.count('1'))[2:]
#     zero_count_2 = bin(n2.count('0'))[2:]
#
#     r = int(one_count_2 + zero_count_2, 2)
#
#     if r == 183:
#         print(n)
#         break;