
from datetime import datetime, date, time
import datetime
#from dateutil.relativedelta import *

output = []

days_header = ['Su','Mo','Tu','We','Th','Fr','Sa']
months_list = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

mo_str = input ("\nEnter Month (format MM): ")
yr_str = input (  "Enter Year (format YYYY):")

d = datetime.datetime(int(yr_str),int(mo_str),1)

#This gets the day of the week for the first day of the month
#Function returns 0=Monday through 6 = Sunday
#If statement adds 1 to all days but Sunday; Sunday is corrected to 0
#Value resulting will be 0=Sunday through 7=Saturday
day1_dow = 0 if datetime.datetime.weekday(d)== 6 else datetime.datetime.weekday(d)+1

#last_day = d + dateutil.relativedelta(day=1, months=+1, days=-1)
#dan = d + datetime.timedelta (months=+1,days=-1) 
last_day = datetime.datetime(int(yr_str)+1, 1 ,1) + datetime.timedelta (days=-1) if mo_str == "12" else datetime.datetime(int(yr_str),int(mo_str)+1 ,1) + datetime.timedelta (days=-1)
last_day_number = int( last_day.strftime ( '%d'))

#print ( "Last Day of month is {0:2d}".format(last_day_number))

#Fills an array of the 42 possible sqaures ont he calendar
for i in range (42):

    if i< day1_dow or (i+1-day1_dow) > last_day_number:
        output.append ("**")
    else:
        output.append ( "{0:2d}".format(i+1-day1_dow))

		
print ( "\n      "+months_list[int ( mo_str)-1]+" {0:%Y}".format(d))
		
		
print ( days_header[0] + " "
      + days_header[1] + " "
      + days_header[2] + " "
      + days_header[3] + " "
      + days_header[4] + " "
      + days_header[5] + " "
      + days_header[6]  )

for i in range(6):

    print ( output [ i*7 + 0 ] + " "
          + output [ i*7 + 1 ] + " "        
          + output [ i*7 + 2 ] + " "        
          + output [ i*7 + 3 ] + " "        
          + output [ i*7 + 4 ] + " "        
          + output [ i*7 + 5 ] + " "        
          + output [ i*7 + 6 ] )

   