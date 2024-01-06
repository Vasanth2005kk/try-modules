import datetime as dt

print(dt.__all__)
print(len(dt.__all__))


#current date and time 
print(dt.datetime.now())

#spcifi time print it

x=dt.datetime.now()
print(x.strftime("%A"))


# Date Time in Python

current_date = dt.date.today()
print("Current Date : ", current_date)

new = dt.date(2021, 10, 25)
print(new)
print("Year : ", new.year)
print("Month : ", new.month)
print("Day : ", new.day)
print("--------------------------------------")
a = dt.time(10, 45, 5, 555505)
print(a)
print("Hour : ", a.hour)
print("minute : ", a.minute)
print("second : ", a.second)
print("microsecond : ", a.microsecond)
print("--------------------------------------")
current_time = dt.datetime.now()
print("Current Time : ", current_time)
print("--------------------------------------")
new = dt.datetime(2021, 5, 31, 12, 2, 10)
print(new)
print(new.date())
print(new.time())
print("--------------------------------------")
current = dt.datetime.now()
new_year = dt.datetime(2022, 1, 1)
difference = new_year - current
print(difference)
print("--------------------------------------")
current = dt.datetime.now()
print(current)
s = current.strftime("%A %b %d %Y")
print(s)

'''

#this using a function == variable_time.strftime()
 
%a 	Weekday, short version ==>	Wed 	
%A 	Weekday, full version ==> Wednesday 	
%w 	Weekday as a number 0-6, 0 is Sunday ==> 3 	
%d 	Day of month 01-31 ==>	31 	
%b 	Month name, short version ==> Dec 	
%B 	Month name, full version ==> December 	
%m 	Month as a number 01-12 ==> 12 	
%y 	Year, short version, without century ==> 18 	
%Y 	Year, full version 	==> 2018 	
%H 	Hour 00-23 	==> 17 	
%I 	Hour 00-12 	==> 05 	
%p 	AM/PM 	==> PM 	
%M 	Minute 00-59 ==> 41 	
%S 	Second 00-59 ==> 08 	
%f 	Microsecond 000000-999999 	==> 548513 	
%z 	UTC offset ==>	+0100 	
%Z 	Timezone 	==> CST 	
%j 	Day number of year 001-366 ==> 365 	
%U 	Week number of year, Sunday as the first day of week, 00-53 ==> 52 	
%W 	Week number of year, Monday as the first day of week, 00-53 ==> 52 	
%c 	Local version of date and time ==> Mon Dec 31 17:41:00 2018 	
%C 	Century	==> 20 	
%x 	Local version of date ==> 12/31/18 	
%X 	Local version of time ==> 17:41:00 	
%% 	A % character ==> % 	
%G 	ISO 8601 year ==> 2018 	
%u 	ISO 8601 weekday (1-7) ==> 1 	
%V 	ISO 8601 weeknumber (01-53) ==> 01

'''