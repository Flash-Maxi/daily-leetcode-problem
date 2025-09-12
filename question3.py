## check for vowel in string ###

class Solution(object):
    def doesAliceWin(self, s):
        v="AEIOUaeiou"
        for char in s:
            if char in v:
                return True
        return False