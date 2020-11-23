# -*- coding: utf-8 -*-

class AgorithmFor100():
    '''Tách số trong chuỗi '123456789' ra để cộng (trừ)
    Lần đầu tách ra thành 1 số và cặp chuỗi. Sau đó gọi hàm đệ quy để tiếp tục
    tách chuỗi và cộng (trừ) với số tiếp theo.
    Cứ tiếp tục như thế cho đến khi hết chuỗi và cho ra kết quả tổng là 100'''
    
    def __init__(self):
        self.tong =[]
    def cho_kq_100(self,s,tong,path=""):
        if len(s)==0 and tong==100:
            self.tong.append(path)
        for i in range(len(s)):
            self.cho_kq_100(s[i+1:],tong+int(s[:i+1]),path+"+"+s[:i+1])
            self.cho_kq_100(s[i+1:],tong-int(s[:i+1]),path+"-"+s[:i+1])

a = AgorithmFor100()
a.cho_kq_100("123456789",0)
for i in a.tong:
    print(i)
