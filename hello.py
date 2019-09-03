import urllib.request
import re

class employee:
    empname="altman"
    html=""
    def __init__(self,name):
        self.empname=name+" is good"

    def displayname(self):
        print(self.empname)
    


for i in range(0,10,1):
    print(i)
print("hello world")
t=employee("atom")
t.displayname()
html=urllib.request.urlopen("https://testportal.iuoooo.com").read()
html=html.decode('utf-8')
#print(html)
pattern="[\s,\S]*"
phone="18382099231"
print(re.match(pattern,html[0:100]).group())
x=input("请输入X:")
y=input("请输入Y:")
print(int(x)*int(y))
arry=['-','-','-','-','-','-','-','-','-','-','-','-','-','-']

for i in range(1,10):
	for j in range(1,10):
		print(str(arry[0:i])+str(int(i)*int(j)))

