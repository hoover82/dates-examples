
###################################################################################
#
# calender.py
# Completed 2017-02-07, Dan Stober
# 
###################################################################################

from datetime import datetime, date, time
import datetime

output = []
days_header = ['Su','Mo','Tu','We','Th','Fr','Sa']
months_list = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

mo_str = input ("\nEnter Month (format MM): ")
yr_str = input (  "Enter Year (format YYYY):")

#Converts inputted strings to a date -- uses the first day of the month
d = datetime.datetime(int(yr_str),int(mo_str),1)

#This gets the day of the week for the first day of the month
#Function returns 0=Monday through 6 = Sunday
#If statement adds 1 to all days except Sunday; Sunday is corrected to 0
#Value resulting will be 0=Sunday through 7=Saturday
day1_dow = 0 if datetime.datetime.weekday(d)== 6 else datetime.datetime.weekday(d)+1

# Get the number of the last day of the month
# Done by adding one month to our dat "d"m subtracting one day (using timedelta), and then extracting the number of that date
#
# TO add one month, we create a new date variable and just add 1 to the month -- unless the month was 12, then we add 1 to the year and use 1 for the month
last_day = datetime.datetime(int(yr_str)+1, 1 ,1) + datetime.timedelta (days=-1) if mo_str == "12" else datetime.datetime(int(yr_str),int(mo_str)+1 ,1) + datetime.timedelta (days=-1)
last_day_number = int( last_day.strftime ( '%d'))

#print ( "Last Day of month is {0:2d}".format(last_day_number))

#Fills an array of the 42 possible squares on the calendar
for i in range (42):

    if i< day1_dow or (i+1-day1_dow) > last_day_number:
        output.append ("**")
    else:
        output.append ( "{0:2d}".format(i+1-day1_dow))

#Once the array is filled we can print the calendar
		
print ( "\n      "+months_list[int( mo_str)-1]+" {0:%Y}".format(d))		
		
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

   