# s = 'egg'
# d1 = {}
# for item, value in enumerate(s):
#     d1[value] = d1.get(value,[]) + [item] #indexing each alphabet in the string... e
# print(d1.values())
#
# t = 'add'
# d2 = {}
# for item, value in enumerate(t):
#     d2[value] = d2.get(value,[]) + [item] #indexing each alphabet in the string... e
# print(d2)
#


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d1 = {}
        d2 = {}
        for item, value in enumerate(s):
            d1[value] = d1.get(value,[]) + [item] #indexing each alphabet in the string... e
        # return print([item])

        for item, value in enumerate(t):
            d2[value] = d2.get(value,[]) + [item]

        if sorted(d1.values()) == sorted(d2.values()):
            return True
        else:
            return False

#TC = O(n)
#SC = O(2)
