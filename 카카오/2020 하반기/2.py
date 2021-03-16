import itertools
orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]

order_dict = {}
for i in orders:
    for j in i:
        order_dict.setdefault(j, 0)
        order_dict[j] += 1
for k,v in order_dict:
    if v >= 2:
        order_dict.pop(k)
print(order_dict)


