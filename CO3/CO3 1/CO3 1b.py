import time
print("current time in sec :",time.time())
print("current time:",time.ctime())
print("current time after 30 sec :",time.ctime(time.time()+30))
print()
t=time.localtime()
print("time t:",t)
print("current hour :",t.tm_hour)
print("current month :",t.tm_mon)
print("current day :",t.tm_mday)
print("current year :",t.tm_year)

