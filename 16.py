# Easy

# def f(n):
#     if n == 1  or n == 0:
#         return 1
#     return f(n - 1) + f(n - 2)
#
# print(f(7))

# 2023

# from functools import lru_cache
#
# @lru_cache(None)
# def f(n):
#     if n < 3:
#         return 1
#     return (n - 1) * f(n-2)
#
#
# for i in range(2026):
#     f(i)
#
# print((f(2026) - 5*f(2024)) / f(2022))

# 2024

# from functools import lru_cache
#
# @lru_cache(None)
# def f(n):
#     if n < 5:
#         return n
#     return 2 * n * f(n-4)
#
# for i in range(13766):
#     f(i)
#
# print((f(13766) - 9 * f(13762)) / f(13758))

# from functools import lru_cache
#
# @lru_cache(None)
# def f(n):
#     if n < 6:
#         return n + 1
#     return  2 * n * f(n-5)
#
# for i in range(137665):
#     f(i)
#
# print((f(137665) - 9 * f(137660)) / f(137655))

def f(n):
    if n >= 5000:
        return n
    if n % 5 != 0:
        return n * f(n+1)
    return n * f(n+2) // 5

print(f(4975) / f(4978))