# from itertools import product, repeat
#
# k = 0
#
# word = ['Ц', 'А', 'П', 'Л', 'Я']
#
# word.sort()
#
# word = ''.join(word)
#
# for x in product(word, repeat=5):
#     s = ''.join(x)
#     k += 1
#     if s.count('А') == 1 and s.count('П') == 2 and s.count('Л') == 0:
#         print(k)
#         break

# from itertools import product, repeat
#
# k = 0
#
# word = 'К О М П Ь Ю Т Е Р'.split()
# word.sort()
# word = ''.join(word)
# for x in product(word, repeat = 5):
#     s = ''.join(x)
#     k += 1
#
#
#     if s[0] != 'Е' and s.count('К') == 2:
#         print(k)
#         break