class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        product,sum=1,0
        while(n>0):
            digit=n%10
            n/=10
            product*=digit
            sum+=digit
        return product-sum
       
        
