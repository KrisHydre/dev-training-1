class Solution_to_100:
    def __init__(self):
        self.total =[]
    def total_to_100(self,s,total,path=""):
        if len(s)==0 and total==100:
            self.total.append(path)
        for i in range(len(s)):
            self.total_to_100(s[i+1:],total+int(s[:i+1]),path+"+"+s[:i+1])
            self.total_to_100(s[i+1:],total-int(s[:i+1]),path+"-"+s[:i+1])

a = Solution_to_100()
a.total_to_100("123456789",0)
for i in a.total:
    print(i)
