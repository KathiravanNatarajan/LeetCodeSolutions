class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num = x 
        rev_digit = 0 
        if x < 0: 
            return False 
        else:
            rev_digit = 0 
            while num > 0:
                rev_digit = rev_digit * 10 + num % 10 
                num = num / 10         
            if rev_digit == x: 
                return True 
			else:
				return False 