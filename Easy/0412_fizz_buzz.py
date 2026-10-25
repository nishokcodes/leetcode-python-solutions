class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        l=[]
        for x in range(1,n+1):
            if x%3==0 and x%5==0:
                l+=["FizzBuzz"]
            elif x%3==0:
                l+=["Fizz"]
            elif x%5==0:
                l+=["Buzz"]
            else:
                l+=[str(x)]
        return l
