class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dict1 = {}

        for w in strs:
            sortedword = "".join(sorted(w))

            if sortedword not in dict1:
                dict1[sortedword] = [w]

            else:
                dict1[sortedword].append(w)

        list1 = []
        for values in dict1.values():
            list1.append(values)
        return list1

    #TC = O(n)
    #SC = O(n)
