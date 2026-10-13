class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = []# to sore the original
        p =[]# to store flipped 
        characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        for i in range(1,len(s)+1):
            if s[-i] in characters:
                p.append(s[-i].lower())
        for i in range(len(s)):
            if s[i] in characters:
                l.append(s[i].lower())
        if p == l:
            return True
        else:
            return False