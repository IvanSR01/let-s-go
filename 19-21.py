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
# from functools import lru_cache
#
# @lru_cache(None)
# def g(h):
#     a, b = h
#     if a + b >= 62:
#         return 'Win'
#     m = [(a+2, b), (a, b+2), (a*2, b), (a, b*2)]
#     if any(g(x) == 'Win' for x in m):
#         return 'P1'
#     if all(g(x) == 'P1' for x in m):
#         return 'V1'
#     if any(g(x) == 'V1' for x in m):
#         return 'P2'
#     if all(g(x) == 'P1' or g(x) == 'P2' for x in m):
#         return 'V2'
#
# print('19:', [i for i in range(1, 55) if g((7, i)) == 'V1'])
# print('20:', [i for i in range(1, 55) if g((7, i)) == 'P2'])
# print('21:', [i for i in range(1, 55) if g((7, i)) == 'V2'])

# from functools import lru_cache
#
# @lru_cache(None)
# def g(h):
#     a, b = h
#
#     if a + b >= 263:
#         return 'Win'
#
#     m = [(a + 1, b), (a, b + 1), (a * 2, b),  (a, b * 2)]
#
#     if any(g(x) == 'Win' for x in m):
#         return 'P1'
#     if any(g(x) == 'P1' for x in m):
#         return 'V1'
#     if any(g(x) == 'V1' for x in m):
#         return 'P2'
#     if all(g(x) == 'P2' or g(x) == 'P1' for x in m):
#         return 'V2'
#
# for i in range(1, 246):
#     print(i, g((17, i)))
#
# print('19:', [i for i in range(1, 246) if g((17, i)) == 'V1'])
# print('20:', [i for i in range(1, 246) if g((17, i)) == 'P2'])
# print('21:', [i for i in range(1, 246) if g((17, i)) == 'V2'])

# from functools import lru_cache
#
# @lru_cache(None)
# def g(h):
#     if h >= 34:
#         return 'Win'
#
#     m = [h + 2, h * 3]
#
#     if any(g(x) == 'Win' for x in m):
#         return 'P1'
#     if all(g(x) == 'P1' for x in m):
#         return 'V1'
#     if any(g(x) == 'V1' for x in m):
#         return 'P2'
#     if all(g(x) == 'P2' or g(x) == 'P1' for x in m):
#         return 'V2'
#
# print('19:', [i for i in range(1, 28) if g(i) == 'P1'])
# print('20:', [i for i in range(1, 28) if g(i) == 'P2'])
# print('21:', [s for s in range(1, 34) if g(s) == 'V2' and g(s) != 'V1'])

# from functools import lru_cache
#
# @lru_cache(None)
# def g(h):
#     a, b, c = h
#
#     if a + b + c >= 50:
#         return 'Win'
#
#     moves = [(a + 1, b, c), (a, b + 1, c), (a, b, c + 1), (a * 2, b, c), (a, b * 2, c), (a, b, c * 2)]
#
#     if any(g(m) == 'Win' for m in moves):
#         return 'P1'
#     if all(g(m) == 'P1' for m in moves):
#         return 'V1'
#     if any(g(m) == 'V1' for m in moves):
#         return 'P2'
#     if all(g(m) == 'P1' or g(m) == 'P2' for m in moves):
#         return 'V2'
#
# print('19:', [i for i in range(1, 40) if g((5, 5, i)) == 'P1'])
# print('20:', [i for i in range(1, 40) if g((5, 5, i)) == 'P2'])
# print('21:', [i for i in range(1, 40) if g((5, 5, i)) == 'V2'])