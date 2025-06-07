# 2, 3, x3: end to >= 41 1 <= s <= 40
# from functools import lru_cache
#
# @lru_cache(None)
# def g(h):
#     m = [h*3, h+3, h+2]
#     if h >= 41:
#         return 'Win'
#     if any(g(x) == 'Win' for x in m):
#         return 'P1'
#     if all(g(x) == 'P1' for x in m):
#         return 'V1'
#     if any(g(x) == 'V1' for x in m):
#         return 'P2'
#     if all(g(x) == 'P1' or g(x) == 'P2' for x in m ):
#         return 'V2'
#
#
# for h in range(1, 41):
#     print(h, g(h))

# 1, 2, 5: end to >= 10 1 S>=11
# from functools import lru_cache
#
# @lru_cache(None)
# def g(h):
#     m = [h-1, h // 3, h-5]
#     if 10 >= h:
#         return 'Win'
#     if any(g(x) == 'Win' for x in m):
#         return 'P1'
#     if all(g(x) == 'P1' for x in m):
#         return 'V1'
#     if any(g(x) == 'V1' for x in m):
#         return 'P2'
#     if all(g(x) == 'P1' or g(x) == 'P2' for x in m ):
#         return 'V2'
#
# print('0:', [h for h in range(1, 200) if g(h) == 'P1'])
# print('19:', [h for h in range(1, 200) if g(h) == 'V2'])
# print('20:', [h for h in range(1, 200) if g(h) == 'P2'])
# print('21:', [h for h in range(1, 200) if g(h) == 'V2'])

# 2, x2
from functools import lru_cache

@lru_cache(None)
def g(h):
    a, b = h
    if a + b >= 62:
        return 'Win'
    m = [(a+2, b), (a, b+2), (a*2, b), (a, b*2)]
    if any(g(x) == 'Win' for x in m):
        return 'P1'
    if all(g(x) == 'P1' for x in m):
        return 'V1'
    if any(g(x) == 'V1' for x in m):
        return 'P2'
    if all(g(x) == 'P1' or g(x) == 'P2' for x in m):
        return 'V2'

print('19:', [i for i in range(1, 55) if g((7, i)) == 'V1'])
print('20:', [i for i in range(1, 55) if g((7, i)) == 'P2'])
print('21:', [i for i in range(1, 55) if g((7, i)) == 'V2'])