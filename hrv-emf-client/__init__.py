#all the imports
import datetime
import random
from threading import Timer
def on():
    time= datetime.datetime.now().isoformat() #current time
    print('on')
    print (time)
    #switch all devices on
def off():
    time= datetime.datetime.now().isoformat() #current time
    print('off')
    print (time)
    #switch all devices off
def end():
    time= datetime.datetime.now().isoformat() #current time
    print("messung end")
    print (time)
def mess():
    f=open('messungerst.txt', 'a')
    prewaitingtime= 60*0.25 #3 minutes waiting at the start of the measurement
    postwaitingtime= 60*0.25 #atleast 3 minutes waiting after 
    totaltime= 60* 1 # 15 minutes total time
    tut= 60* 0.25 # 5 minutes with 
    maxtimeshift=totaltime-prewaitingtime-postwaitingtime-tut
    start=random.randint(0,maxtimeshift)+prewaitingtime
    stop=start+tut
    print(start)
    #switch all the devices off
    time= datetime.datetime.now() #current time
    print (time)
    t = Timer(start, on)
    t.start()
    t2= Timer(stop, off)
    t2.start()
    t3= Timer(totaltime, end)
    t3.start()
    f.write('\nNeue Messung Beginn: ')
    f.write(time.isoformat())
    timestart= time + datetime.timedelta(seconds=start)
    timestop= time + datetime.timedelta(seconds=stop)
    timeend= time+datetime.timedelta(seconds=totaltime)
    f.write("\nStart: ")
    f.write(timestart.isoformat())
    f.write("\nStop: ")
    f.write(timestop.isoformat())
    f.write("\nEnd: ")
    f.write(timeend.isoformat())
    f.close()    
