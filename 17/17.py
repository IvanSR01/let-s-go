# a = [int(s) for s in open('17.txt')]
# a238 = max([x for x in a if x % 1000 == 238])
# count = 0
# s3 = []
# for i in range (len(a) - 2):
#     troika = [a[i] , a[i+1] , a[i+2]]
#     a3 = [x for x in troika if x % 3 == 0]
#     a5 = [x for x in troika if x % 5 == 0]
#     raz5 = [x for x in troika if len(str(x)) == 5]
#     if sum(troika) > a238:
#         if len(a3) > len (a5):
#             if 0 < len(raz5) < 3:
#                 s3.append(sum(troika))
# print(len(s3),max(s3))

c = 0
max_sum = 0
a = [int(s) for s in open('17-2.txt')]
amin5 = min([x for x in a if str(abs(x))[0] == '5' and len(str(abs(x))) == 3])

i = len(a) - 1

s3 = []
for i in range (len(a) - 2):
    troika = [a[i] , a[i+1] , a[i+2]]
    a_4 = [x for x in troika if abs(x)%10 == 4 ]
    asum = sum(troika)
    if len(a_4) == 1:
        if asum % amin5 != 0:
            s3.append(sum(troika))
print(len(s3),max(s3))


