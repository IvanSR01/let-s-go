#
#
# def f9(n):
#     k1 = 0
#     while n > 0:
#         if n % 27 == 1:
#             k1 += 1
#         n = n // 27
#     return k1
#
# def f10(n):
#     k1 = 0
#     while n > 0:
#         if n % 27 > 8:
#             k1 += 1
#         n = n // 27
#     return k1
#
# def f11(n):
#     k1 = 0
#     while n > 0:
#         k1 += n % 27
#         n = n // 27
#     return k1
#
#
# n = 6*343**1156 - 5*49**1147 + 4*7**1153 - 875
#
# print(f9(n))
# print(f10(n))
# print(f11(n))

# for x in range(19):
#     s1 = int('9879731', 19) + x * 19**5
#     s2 = int('3614', 19) + x * 19**2
#
#     if (s1 + s2 ) % 18 == 0:
#         print(x % 18)
#         break

for x in range(22):
    t1 = int('9879641', 22) + x * 22**5
    t2 = int('2543', 22) + x * 22**2
    t3 = int('635', 22) + x * 22**1

    if (t1 + t2 + t3) % 21 == 0:
        print(x % 21)