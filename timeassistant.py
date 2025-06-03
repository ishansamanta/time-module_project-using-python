from datetime import datetime                                      #1. IMPORTING DATE TIME FROM DATETIME MODULE
import pytz                                                        #2.IMPORTING PYTZ library to hold the time stamp format
india_tz = pytz.timezone('Asia/Kolkata')                           #3.you can change the "Asia/Kolkata" to your region  
current_time = datetime.now(india_tz) 
timestamp = current_time.strftime("%H: %M: %S")                    #5.strftime holds the time in ("%H: %M: %S") format
print("Current Time =", timestamp)                                 #6.Displays the timestamp recorded
hr= current_time.strftime("%H") 
mn= current_time.strftime("%M")
sc= current_time.strftime("%S")
if int(hr)>=12:
  print('PM')
if(int(hr)>12 and int(hr)<15):
  print('Good Afternoon')  
elif(int(hr)>=15 and int(hr)<20):
  print('Good Evening')

elif (int(hr)>=20 and int(hr)<24):
  print('Good Night')

else:
  print('Good Morning')
  print('Have a nice day')

#APOLOGISING FOR NO README FILE AVAILABLE
################################################################################################################################
