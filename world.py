import datetime
import threading
import sys
from hello import employee
b=employee("altman")
b.displayname()
print(sys.path)

def fun_timer():
	print(datetime.datetime.now())
	
global timer	
timer=threading.Timer(10,fun_timer)
timer.start()


