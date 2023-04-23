class Solution:
    def isPalindrome(self, s: str) -> bool:
        nums = ['0','1','2','3','4','5','6','7','8','9']
        new_s = ""
        s = s.lower()
        for l in s:
            if (ord(l)>=97 and ord(l)<=122) or l in nums:
                new_s = new_s + l
                
        j = 0
        for i in range(len(new_s)-1, -1, -1):
            if new_s[i] != new_s[j]:
                return False
            j = j +1
        return True