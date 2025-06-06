# 9_12

# file = open('9_12.txt')
# cnt = 0
#
# for s in file:
#     nums = [int(x) for x in s.split()]
#
#     max_num = max(nums)
#
#     nums.remove(max_num)
#
#     if max_num * max_num > 2 * nums[0] * nums[1]:
#         cnt += 1
#
# print(cnt)

# 9_13

# file = open('9_13.txt')
# cnt = 0
#
# for s in file:
#     nums = [int(x) for x in s.split()]
#
#     nums.sort()
#
#     if nums[0] + nums[1] + nums[2] < nums[3] and len(set(nums)) == len(nums):
#         cnt += 1
#
# print(cnt)

# file = open('9_13.txt')
# cnt = 0
#
# for s in file:
#     nums = [int(x) for x in s.split()]
#
#     max_num = max(nums)
#
#     nums.remove(max_num)
#
#     sum_nums = sum(nums)
#
#     nums.append(max_num)
#
#     if sum_nums > max_num and len(set(nums)) == len(nums) - 1:
#         cnt += 1
#
# print(cnt)

# file = open('9_9832.txt')
# cnt = 0
#
# for s in file:
#     nums = [int(x) for x in s.split()]
#
#     dp = []
#
#     for n in nums:
#         if nums.count(n) == 2:
#             dp.append(n)
#
#     dp = list(set(dp))
#
#     if len(dp) == 2:
#         origin = list(set(nums))
#
#         origin.remove(dp[0])
#         origin.remove(dp[1])
#
#         if len(origin) == 3 and nums.count(max(nums)) == 1:
#             cnt += 1
# print(cnt)

# 09_statok23

# file = open('09_statok23.txt')
# cnt = 0
#
# for s in file:
#     nums = [int(x) for x in s.split()]
#
#     origin = len(set(nums))
#
#     if origin == len(nums):
#         min_num = min(nums)
#         nums.remove(min_num)
#
#         max_num = max(nums)
#         nums.remove(max_num)
#
#         if sum(nums) / len(nums) > (min_num + max_num) / 2:
#             cnt += 1
#
# print(cnt)

# 09_stat_yanv25

# file = open('09_stat_yanv25.txt')
# cnt = 0
#
# for s in file:
#     nums = [int(x) for x in s.split()]
#
#     len_nums = len(nums) // 2
#
#     first = nums[:len_nums]
#     second = nums[len_nums:]
#
#     max_num = max(nums)
#
#     if nums.count(max_num) == 1 and max_num in first and (sum(first) / len(first)) < (sum(second) / len(second)):
#         cnt += 1
#
# print(cnt)

# 09_stat_mart25
# file = open('09_stat_mart25.txt')
# cnt = 0
#
# for s in file:
#     nums = [int(x) for x in s.split()]
#
#     arp = sum(nums) / len(nums)
#
#     vis_ch = []
#     vis_nch = []
#
#     nums_ch = []
#     nums_nch = []
#
#     for n in nums:
#         if n > arp:
#             if n % 2 == 0:
#                 vis_ch.append(n)
#             else:
#                 vis_nch.append(n)
#         if n % 2 == 0:
#             nums_ch.append(n)
#         else:
#             nums_nch.append(n)
#
#     if len(vis_ch) > len(vis_nch) and sum(nums_ch) < sum(nums_nch):
#         cnt += 1
#
# print(cnt)
