import pymysql
conn=pymysql.connect(host='39.96.69.194',port=3306,user='root',passwd='1234QWER!@#$',database="amp_ebc",charset='utf8')
#创建游标
cursor=conn.cursor()
#cursor.execute("CREATE DATABASE altman")
#cursor.execute("CREATE TABLE table(name varchar(255))")
cursor.execute("select * from employee limit 10")
#获取所有记录
result=cursor.fetchall()

for i in result:
	print(i) 
print(result)
conn.commit()
cursor.close()
conn.close()
