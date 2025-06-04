# def f(a, b):
#     if a == b:
#         return 1
#     if a > b or a == 15 or a == 30:
#         return 0
#     return f(a + 2, b) + f(a + 3, b) + f(a * a, b)
#
#
# print(
#     f(3, 10) * f(10, 20) * f(20, 38)
# )

# from functools import *
#
# @lru_cache(None)
#
# def f(a, b, nch, ch):
#     if a == b and ch > nch:
#         return 1
#     if a == b and ch < nch:
#         return 0
#     if a > b:
#         return 0
#     return f(a+2, b, nch + ((a+2) % 2), ch + (not ((a+2) % 2))) + f(a+3, b, nch + ((a+3) % 2), ch + (not ((a+3) % 2))) + f(a*4, b, nch, ch + 1)
#
# print(sum(map(int, str(f(1, 100, 1, 0)))))

# def f(a, b):
#     if a == b:
#         return 1
#     if a < b:
#         return 0
#     return f(a//3, b) + f(a-1, b) + f(a-5, b)
#
# print(f(46, 22) * f(22, 5))

# def f(a, b):
#     if a == b:
#         return 1
#     if a < b or a == 19 or a == 17:
#         return 0
#     return f(a-3, b) + f(a-2, b)
#
# print(f(43, 7))
#
# def f(a, b):
#     if a == b:
#         return 1
#     if a < b:
#         return 0
#     return f(a - 3, b) + f(a - 2, b) + f(a - 1, b)
#
# print(f(36, 28) * f(28, 26) * f(26, 13))

# from functools import *
#
# @lru_cache(None)
#
# def f(a, b, A):
#     if a == b:
#         return 1
#     if a > b + 1:
#         return 0
#     if A == 1:
#        return f(a * 2, b, 0) + f(a * 3, b, 0)
#     return f(a-1, b, 1) + f(a*2, b, 0) + f(a*3, b, 0)
#
#
# print(f(3, 15, 0))

# def f(a, b):
#     if a == b:
#         return 1
#     if a > b:
#         return 0
#     return f(a + 1,b) + f(a*2,b) + f(a*3,b)
#
# print(f(2, 12) * f(12, 28))

# def f(a, b):
#     if a == b:
#         return 1
#     if a > b or a == 28:
#         return 0
#     return f(a+1,b) + f(a*2, b)
#
# print(f(2, 10) * f(10, 34))

# def f(a, b):
#     if a == b:
#         return 1
#     if a > b or a == 32:
#         return 0
#     return f(a+3,b) + f(a*2, b)
#
# print(f(1, 16) * f(16,41))

# warning смотри что пишешь
# def f(a, b):
#     if a == b:
#         return 1
#     if a > b or a == 10 or a == 15:
#         return 0
#     return f(a+1,b) + f(a+2,b) + f(a+3,b)
#
# print(f(5, 11) * f(11, 18))

# def f(a, b):
#     if a < b:
#         return 0
#     if a == b:
#         return 1
#     return f(a - 1, b) + f(a // 2, b)
#
#
# print(f(30, 10) * f(10, 1))

# def f(a, b):
#     if a < b:
#         return 0
#     if a == b:
#         return 1
#     return f(a-1, b) + f(a//3, b)
#
# print(f(37, 10) * f(10, 2))