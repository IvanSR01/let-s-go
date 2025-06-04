#
# n = '2' + ('0' * 1348)
#
# while ('2' in n) or ('200' in n):
#     if '200' in n:
#         n = n.replace('200', '0002', 1)
#     else:
#         n = n.replace('2', '00', 1)
#
# print(n.count('0'))

# s = 'AB' * 403
#
# while 'AAA' in s or 'BBB' in s or 'AB' in s:
#     s = s.replace('AAA', 'BC', 1)
#     s = s.replace('BBB', 'DA', 1)
#     s = s.replace('AB', 'BA', 1)
#     s = s.replace('CD', 'BBA', 1)
#
# print('B', s.count('B'))
# print('C', s.count('C'))

# def func(s):
#     while '31' in s or '411' in s or '1111' in s:
#         if '31' in s:
#             s = s.replace('31', '1', 1)
#         if '411' in s:
#             s = s.replace('411', '13', 1)
#         if '1111' in s:
#             s = s.replace('1111', '4', 1)
#     res = sum(map(int, s))
#
#     return res
#
# for n in range(4, 10000):
#     s = '4' + ('1' * n)
#
#     res = func(s)
#
#     if res**0.5 == int(res**0.5):
#         print(n)
#         break;

# s = '1' * 77
#
# while '111' in s:
#     s = s.replace('111', '2', 1)
#     s = s.replace('222', '3', 1)
#     s = s.replace('333', '1', 1)
#
# print(s)

# s = '1' * 81
#
# while '11111' in s or '888' in s:
#     if '11111' in s:
#         s = s.replace('11111', '88', -1)
#     else:
#         s = s.replace('888', '8', -1)
#
# print(s)

# s = '8' * 100
#
# while '888' in s or '77' in s:
#     if '888' in s:
#         s = s.replace('888', '8777', 1)
#     else:
#         s = s.replace('77', '8', 1)
#
# print('8', s.count('8'), '7', s.count('7'))

# s = '22' + ('1' * 2023) + '22'
#
# while '211' in s or '112' in s:
#     s = s.replace('11', '1', 1)
#     if '21' in s:
#         s = s.replace('21', '12', 1)
#     else:
#         s = s.replace('12', '1', 1)
# print(s)

# col = []
#
# for n in range(2, 1000):
#     s = '8' * n
#
#     while '555' in s or '888' in s:
#         s = s.replace('555', '8', 1)
#         s = s.replace('888', '55', 1)
#
#     col.append(s)
#
# print(set(col))

# for n in range(200, 1000):
#     s = '1' * n
#
#     while '111' in s or '222' in s:
#         s = s.replace('111', '22', 1)
#         s = s.replace('222', '1', 1)
#
#     if s.count('2') == 0:
#         print(n)
#         break;