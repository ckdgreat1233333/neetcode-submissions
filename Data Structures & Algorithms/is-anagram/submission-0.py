class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        j =[]
        k =[]
        for i in range(len(s)):
            j.append(s[i])
        for i in range(len(t)):
            k.append(t[i])
        j.sort()
        k.sort()
        if j == k:
            return True
        else:
            return False
        