class Solution:
    def addDigits(self, num):
        while num >= 10:
            digit_sum = 0
            while num > 0:
                digit = num % 10
                digit_sum += digit
                num //= 10
            num = digit_sum
        return num
