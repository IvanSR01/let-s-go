
# easy test
# for x in range(1, 5):
#     if (((x < 5) <= (x < 3)) and ((x < 2) <= (x < 1))) == True:
#         print(x)
#
# A = range(10, 15)
# k = 0
# for x in range(1, 1000):
#     if (((x in A) <= (x in range(25, 30))) or (x in range(15, 20))) == True:
#         k += 1
#
# print(k)

# Hard

# for A in range(1, 1000):
#     k = 0
#     for x in range(1, 100):
#         for y in range(1, 100):
#             if(((A >= y*y) <= (10 >= y)) and ((9 >= x) <= (A > x*x))) == True:
#                 k += 1
#     if k == 99 * 99:
#         print(A)
#         break