#
# from ipaddress import *
#
# ip = ip_network('192.168.32.160/255.255.255.240', 0)
#
# k = 0
# for ad in ip:
#     ad2 = bin(int(ad))[2:].zfill(32)
#
#     if int(ad2) % 2 != 0:
#         k += 1
#
# print(k)

# from ipaddress import  *
#
# net = ip_network('192.168.32.160/255.255.255.248', 0)
#
# k = 0
#
# for ad in net:
#     ad2 = bin(int(ad))[2:].zfill(32)
#
#     if int(ad2) % 3 == 0:
#         k += 1
#
# print(k)

# from ipaddress import *
#
# net = ip_network('192.168.32.160/255.255.255.240', 0)
#
# k = 0
#
# for ad in net:
#     ad2 = bin(int(ad))[2:].zfill(32)
#
#     if ad2.count('1') == 10:
#         k +=1
#
# print(k)

# from ipaddress import *
#
# net = ip_network('123.8.0.0/255.248.0.0', 0)
#
# max_ad = 0
#
# for ad in net:
#     ad2 = bin(int(ad))[2:]
#
#     count = ad2.count('1')
#
#     max_ad = max(max_ad, count)
#
# print(max_ad)

# from ipaddress import *
#
# net = ip_network('90.65.32.0/255.255.224.0', 0)
#
# c = 0
#
# for ad in net:
#     ad2 = bin(int(ad))[2:].zfill(32)
#
#     if ad2.count('1') == ad2.count('0'):
#         c += 1
#
# print(c)

# from ipaddress import *
#
# mink = 10*10
#
# for mask in range(32, -1, -1):
#     net1 = ip_network('154.63.206.129/' + str(mask), 0)
#     net2 = ip_network('154.63.100.75/' + str(mask), 0)
#     if net1.network_address == net2.network_address:
#         print(net1.network_address)
#         k = 0
#         for ad in net1:
#             ad2 = bin(int(ad))[2:]
#
#             if ad2.count('1') % 2 == 0:
#                 k += 1
#
#             print(k)
#         mink = min(mink, k)
#         break
#
# print(mink)

# from ipaddress import *
#
# mink = 10*10
#
# for mask in range(32, -1, -1):
#     net1 = ip_network('98.162.75.91/' + str(mask), False)
#     net2 = ip_network('98.162.75.64/' + str(mask), False)
#
#     if net1.network_address == net2.network_address:
#         print(net1.num_addresses)
#         break


# from ipaddress import *
#
# mink = 10*10
#
# for mask in range(32, -1, -1):
#     net1 = ip_network('188.162.72.94/' + str(mask), False)
#     net2 = ip_network('188.162.72.64/' + str(mask), False)
#
#     if net1.network_address == net2.network_address:
#         print(net1.num_addresses)
#         break
#

# from ipaddress import ip_network
#
# mask_count = 0
#
# for mask in range(32, -1, -1):
#     net1 = ip_network('198.162.201.94/' + str(mask), False)
#     net2 = ip_network('198.162.192.0/' + str(mask), False)
#
#     print(net1.network_address, net2.network_address)
#
#     if net1.network_address == net2.network_address:
#         mask_count += 1
#
# print(mask_count)

# from ipaddress import *
#
# net = ip_network('255.255.255.224/255.255.255.224', 0)
#
# print(net.num_addresses)
#

# from ipaddress import *
#
# net = ip_network('222.222.188.111/255.255.252.0', 0)
# k = 0
# for ad in net:
#     if ad == ip_address('222.222.188.111'):
#         print(k)
#         break
#     k += 1

# from ipaddress import *
#
# net = ip_network('166.192.0.0/255.252.0.0', 0)
#
# k = 0
#
# for ad in net:
#     ad2 = bin(int(ad))[2:].zfill(32)
#
#     if ad2.count('1') % 2 != 0:
#         k += 1
#
# print(k)
