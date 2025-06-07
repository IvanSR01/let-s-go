from fnmatch import *
from pdb import runctx


# def nechd(i: int):
#     d = []
#
#     for n in range(1, int(i**0.5)):
#         if i % n == 0:
#             if n % 2 != 0:
#                 d.append(n)
#             if i // n != n and (i // n) % 2 != 0:
#                 d.append(i // n)
#
#     return d
#
# for i in range(100000 + 1, 10 ** 6):
#     k = 0
#     nd = nechd(i)
#     if fnmatch(str(i), '1*1?2') and len(nd) == 3:
#         k += 1
#         if k < 5:
#             print(i, sum(nd))
#

# from fnmatch import fnmatch
# from math import isqrt
#
# def isEasyInt(n: int):
#     if n < 2:
#         return False
#     for i in range(2, isqrt(n) + 1):
#         if n % i == 0:
#             return False
#     return True
#
# def p(n: int):
#     nums = [int(x) for x in str(n)]
#     result = 1
#     for i in nums:
#         result *= i
#     return result
#
# for i in range(1234, 10**9 + 1, 1234):
#     if fnmatch(str(i), '24?127*0') and isEasyInt(p(i)):
#         print(i, i // 1234)
