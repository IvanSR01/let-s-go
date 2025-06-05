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

# for A in range(1, 1000):
#     k = 0
#     for x in range(1, 100):
#         for y in range(1, 100):
#             if(((A >= y*y) <= (12 > y)) and ((11 > x) <= (A > x*x))) == True:
#                 k += 1
#     if k == 99 * 99:
#         print(A)
#         break;

# for A in range(1, 200):
#     k = 0
#     for x in range(1, 100):
#         for y in range(1, 100):
#             if (((x < 5) <= (A >= x * x)) and ((A >= y * y) <= (7 >= y))) == True:
#                 k += 1
#     if k == 99 * 99:
#         print(A)
#         break

# for A in range (1, 150):
#     k = 0
#     for x in range(1, 100):
#         for y in range(1, 100):
#             if (((A >= x) <= (x * x < 81)) and ((49 >= y * y) <= (A >= y))) == True:
#                 k += 1
#     if k == 99 * 99:
#         print(A)

# very hard

# collection = []
#
# for start in range(-100, 100):
#     for end in range(start + 1, 100):
#         A = [i for i in range(start, end)]
#         flag = True
#         for x in range(-200, 200):
#             if not (((x in A) <= (x**2 <= 64)) and ((x**2 - 48 <= 2 * x) <= (x in A))):
#                 flag = False
#                 break
#         if flag:
#             collection.append(end - 1 - start)
#
# print(min(collection))

# def delt(n, m):
#     if n % m == 0:
#         return 1
#     return 0
# for A in range(1, 1000):
#     flag = True
#     for x in range(1, 1000):
#         if((not delt(x, A)) <= (delt(x, 6) <= (not delt(x, 9)))) == False:
#             flag = False
#             break
#     if flag:
#         print(A)

# P = [i for i in range(7, 64)]
# Q = [i for i in range(38, 100)]
# R = [i for i in range(85, 120)]
#
# collection = []
#
# for start in range(0, 150):
#     for end in range(start + 1, 150):
#         A = [i for i in range(start, end)]
#
#         flag = True
#
#         for x in range(1, 200):
#             if ((x in Q) <= ((not(x in P)) <= (((not (x in R)) and (not (x in A))) <= (not(x in Q))))) == False:
#                 flag = False
#                 break
#
#         if flag:
#             collection.append(len(A))
#
# print(min(collection))

