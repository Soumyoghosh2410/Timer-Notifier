import time
from plyer import notification
t1=int(input("How many hours: "))
if t1>24 or t1<0:
    print("Stop the cap")
t2=int(input("How many minutes: "))
if t2>59 or t1<0:
    print("Stop the cap")
t3=int(input("How many seconds: "))

t4=60*t2
t5=3600*t1
tt=t3+t4+t5
if __name__=="__main__":
    while True:
        notification.notify(
            title="TIME'S UP !!",
            message="Its been like "+str(t1)+" hrs "+str(t2)+" minutes "+str(t3)+" seconds ",
            timeout=10

        )
        time.sleep(tt)
        