class Solution(object):
    def groupAnagrams(self, strs):
        myDict = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key in myDict:
                myDict[key].append(word)
            else:  
                myDict[key] = [word]
        return list(myDict.values())