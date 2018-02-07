

from datetime import datetime, date, time
import datetime
#from dateutil.relativedelta import *

output = []

days_header = ['Su','Mo','Tu','We','Th','Fr','Sa']

mo_str = input ("\nEnter Month (format MM): ")
yr_str = input (  "Enter Year (format YYYY):")

d = datetime.datetime(int(yr_str),int(mo_str),1)

#This gets the day of the week for the first day of the month
#Function returns 0=Monday through 6 = Sunday
#If statement adds 1 to all days but Sunday; Sunday is corrected to 0
#Value resulting will be 0=Sunday through 7=Saturday
day1_dow = 0 if datetime.datetime.weekday(d)== 6 else datetime.datetime.weekday(d)+1

#last_day = d + dateutil.relativedelta(day=1, months=+1, days=-1)

for i in range (42):

    if i< day1_dow:
        output.append ("**")
    else:
        output.append ( "{0:2d}".format(i+1-day1_dow))

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

   
