#!/usr/bin/python

#You are given the following information, but you may prefer to do some research for yourself.

 #   1 Jan 1900 was a Monday.
 #   Thirty days has September,
 #   April, June and November.
 #   All the rest have thirty-one,
 #   Saving February alone,
 #   Which has twenty-eight, rain or shine.
 #   And on leap years, twenty-nine.
 #   A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

weekday = 2
total = 0
for year in range(1900,2000+1):
	for month in range(1,12+1):
		if month in (4,6,9,11):
			days = 30
		elif month in (1,3,5,7,8,10,12):
			days = 31
		elif year%4==0 and not (year%100==0 and year%400!=0):
			days = 29
		else:
			days = 28

		print "month:" + str(month) + "/ " + str(days) + " days / 1st day on " + str(weekday)
			
		while (days>=0):
			days -= 7

		#print days
		
		while days<0:
			weekday-=1
			if (weekday==0):
				weekday=7
			days+=1

		if weekday == 1 and year>=1901:
			total+=1
			print "01/" + str(month) + "/" + str(year) 
			
print total
