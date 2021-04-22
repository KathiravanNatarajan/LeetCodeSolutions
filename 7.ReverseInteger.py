class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        reversed_digit = 0
        num = x 
        if x < 0: 
            x = -1 * x
        while x > 0:
            reversed_digit = reversed_digit * 10 + x % 10
            x = x / 10
        if num <=-2147483648 or num>=2147483647 or reversed_digit >= 2147483647 or reversed_digit <= -2147483648:
            return 0
        if num < 0: 
            return -1 * reversed_digit
        else:
            return reversed_digit